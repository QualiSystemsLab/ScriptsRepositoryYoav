/*  
 * --------------------------------------- 
 * This query is for CloudShell Apps consumption. 
 * Make sure to fill the @QueryStart and @QueryEnd at the end of the query to filter the rigth timeframe.
 * Make sure to provide the rigth date format. 
 * --------------------------------------- 
 */ 

/* 
      <<<<< REMOVE THIS COMMENT ONCE TESTED >>>>>
	  Testing notes:
      Check for deleted users 
      Check for deleted Topologies 
      Check for deleted Sandboxes 
      Check for active sandbox 
      Check for sandboxes that started before the timeframe 
      Check for sandboxes that started during the timeframe 
      Check for completed sandboxes that failed to delete apps (teardown failed) - apps still exists
      Check for completed sandboxes that failed to delete apps (teardown failed) - apps deleted manually
*/ 

PRINT N'Create consumption_temp_function function' 

go 

CREATE FUNCTION consumption_temp_function (@QueryStart datetime, 
                                           @QueryEnd   datetime) 
returns TABLE 
AS 
    RETURN ( 
      WITH apps_uptime_in_sandbox 
           AS (SELECT RL.Id, 
                      RL.CreatedInReservationId AS SandboxId, 
                      RSL.ReservationName, 
                      RL.Created, 
                      RL.Deleted, 
                      RSL.StartDate, 
                      RSL.ActualEndDate 
               FROM   ResourceLog RL 
                      Join ReservationSummaryLog
                           RSL 
                        On RL.CreatedInReservationId = RSL.ReservationId 
               Where  DeployedResourceLogId is not null -- Show only apps  
                      And ( RL.Deleted is not null 
                             or RSL.ActualEndDate is not null ) 
                      And ( RSL.StartDate <= @QueryEnd 
                            And RSL.ActualEndDate >= @QueryStart ) 
              --only in the timeframe provided 
              ) 
      Select distinct apps.SandboxId, 
                      RSL.ReservationName, 
                      RSL.DomainName, 
                      RSL.StartDate, 
                      RSL.ActualEndDate, 
                      UL.Username, 
                      TL.Name                          AS "Topology Name", 
                      Count(apps.Id) 
                        over ( 
                          partition by apps.SandboxId) AS number_of_apps, 
                      Sum (CASE 
                             WHEN apps.Deleted > apps.ActualEndDate THEN ( 
                             -- Sandbox ended prior to apps deletion 
                             Datediff(minute, apps.Created, 
                             apps.ActualEndDate) ) 
                             WHEN apps.Deleted is null THEN ( 
                             -- Failed to delete apps 
                             Datediff(minute, apps.Created, 
                             apps.ActualEndDate) ) 
                             WHEN apps.ActualEndDate is null THEN ( 
                             --Active Sandbox 
                             Datediff(minute, apps.Created, Getdate()) 
                             ) 
                             ELSE Datediff(minute, apps.Created, apps.Deleted) 
                           END) 
                        over ( 
                          partition by apps.SandboxId) AS 
                      total_apps_in_sandbox_minutes 
       from   apps_uptime_in_sandbox AS apps 
              Join ReservationSummaryLog RSL 
                On apps.SandboxId = RSL.ReservationId 
              Left Join UserLog UL 
                     On UL.Id = RSL.UserId 
              Left Join TopologyLog TL 
                     On TL.Id = RSL.TopologyId 
      ); 

go 

DECLARE @QueryStart AS DATETIME 
DECLARE @QueryEnd AS DATETIME 

SET @QueryStart = CONVERT(varchar, '2018-10-02', 20) -- Input format: yyyy-mm-dd 
SET @QueryEnd = Dateadd(day, 1, CONVERT(varchar, '2018-10-02', 20)); -- Input format: yyyy-mm-dd 

SELECT * 
FROM   consumption_temp_function (@QueryStart, @QueryEnd); 

SELECT Sum(total_apps_in_sandbox_minutes) AS "Total Consumption" 
FROM   consumption_temp_function (@QueryStart, @QueryEnd); 

PRINT N'Drop consumption_temp_function function' 

DROP FUNCTION consumption_temp_function; 