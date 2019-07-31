import cloudshell.api.cloudshell_api as api

class userCreator():
    def __init__(self):   # credentials
        username = 'admin'
        password = 'admin'
        server = 'localhost'
        domain = 'Global'
        # create CS API session
        self.session = api.CloudShellAPISession(
            host=server,
            username=username,
            password=password,
            domain=domain
        )

    def add_external_user(self, username, password, email):
        self.session.AddNewUser(
            username=username,
            password=password,
            email=email,
            isActive=True,
            isAdmin=False
        )
        self.session.UpdateUsersLimitations(
            userUpdateRequests=[api.UserUpdateRequest(
                Username=username,
                MaxConcurrentReservations='2', # max allowed concurrent reservations
                MaxReservationDuration='12' # in hours
            )]
        )
        self.session.AddUsersToGroup(
            usernames=[username],
            groupName='Regular Users'
        )