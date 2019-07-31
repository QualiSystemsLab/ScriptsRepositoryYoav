import cloudshell.api.cloudshell_api as api

username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'

resid = '35990793-82aa-4829-87ca-4c2456c8c6c1'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

restricted = [
'Standard_A0', 'Standard_A1', 'Standard_A2', 'Standard_A3','Standard_A5','Standard_A4','Standard_A6','Standard_A7','Basic_A0','Basic_A1','Basic_A2','Basic_A3','Basic_A4','Standard_D1','Standard_D2','Standard_D3','Standard_D4','Standard_D11','Standard_D12','Standard_D13','Standard_D14','Standard_A1_v2','Standard_A2m_v2','Standard_A2_v2','Standard_A4m_v2','Standard_A4_v2','Standard_A8m_v2','Standard_A8_v2','Standard_DS1','Standard_DS2','Standard_DS3','Standard_DS4','Standard_DS11','Standard_DS12','Standard_DS13','Standard_DS14','Standard_PB6s','Standard_D1_v2','Standard_D2_v2','Standard_D3_v2','Standard_D4_v2','Standard_D5_v2','Standard_D11_v2','Standard_D12_v2','Standard_D13_v2','Standard_D14_v2','Standard_D15_v2','Standard_D2_v2_Promo','Standard_D3_v2_Promo','Standard_D4_v2_Promo','Standard_D5_v2_Promo','Standard_D11_v2_Promo','Standard_D12_v2_Promo','Standard_D13_v2_Promo','Standard_D14_v2_Promo','Standard_F1','Standard_F2','Standard_F4','Standard_F8','Standard_F16','Standard_B1ls','Standard_B1ms','Standard_B1s','Standard_B2ms','Standard_B2s','Standard_B4ms','Standard_B8ms','Standard_DS1_v2','Standard_DS2_v2','Standard_DS3_v2','Standard_DS4_v2','Standard_DS5_v2','Standard_DS11-1_v2','Standard_DS11_v2','Standard_DS12-1_v2','Standard_DS12-2_v2','Standard_DS12_v2','Standard_DS13-2_v2','Standard_DS13-4_v2','Standard_DS13_v2','Standard_DS14-4_v2','Standard_DS14-8_v2','Standard_DS14_v2','Standard_DS15_v2','Standard_DS2_v2_Promo','Standard_DS3_v2_Promo','Standard_DS4_v2_Promo','Standard_DS5_v2_Promo','Standard_DS11_v2_Promo','Standard_DS12_v2_Promo','Standard_DS13_v2_Promo','Standard_DS14_v2_Promo','Standard_F1s','Standard_F2s','Standard_F4s','Standard_F8s','Standard_F16s','Standard_D2_v3','Standard_D4_v3','Standard_D8_v3','Standard_D16_v3','Standard_D32_v3','Standard_D2s_v3','Standard_D4s_v3','Standard_D8s_v3','Standard_D16s_v3','Standard_D32s_v3','Standard_D64_v3','Standard_E2_v3','Standard_E4_v3','Standard_E8_v3','Standard_E16_v3','Standard_E20_v3','Standard_E32_v3','Standard_E64i_v3','Standard_E64_v3','Standard_D64s_v3','Standard_E2s_v3','Standard_E4-2s_v3','Standard_E4s_v3','Standard_E8-2s_v3','Standard_E8-4s_v3','Standard_E8s_v3','Standard_E16-4s_v3','Standard_E16-8s_v3','Standard_E16s_v3','Standard_E20s_v3','Standard_E32-8s_v3','Standard_E32-16s_v3','Standard_E32s_v3','Standard_E64-16s_v3','Standard_E64-32s_v3','Standard_E64is_v3','Standard_E64s_v3','Standard_HB60rs','Standard_NV6','Standard_NV12','Standard_NV24','Standard_NV6_Promo','Standard_NV12_Promo','Standard_NV24_Promo','Standard_L8s_v2','Standard_L16s_v2','Standard_L32s_v2','Standard_L64s_v2','Standard_L80s_v2','Standard_F2s_v2','Standard_F4s_v2','Standard_F8s_v2','Standard_F16s_v2','Standard_F32s_v2','Standard_F64s_v2','Standard_F72s_v2','Standard_NC6s_v3','Standard_NC12s_v3','Standard_NC24rs_v3','Standard_NC24s_v3','Standard_G1','Standard_G2','Standard_G3','Standard_G4','Standard_G5','Standard_GS1','Standard_GS2','Standard_GS3','Standard_GS4','Standard_GS4-4','Standard_GS4-8','Standard_GS5','Standard_GS5-8','Standard_GS5-16','Standard_L4s','Standard_L8s','Standard_L16s','Standard_L32s','Standard_NC6','Standard_NC12','Standard_NC24','Standard_NC24r','Standard_NC6_Promo','Standard_NC12_Promo','Standard_NC24_Promo','Standard_NC24r_Promo','Standard_H8','Standard_H8_Promo','Standard_H16','Standard_H16_Promo','Standard_H8m','Standard_H8m_Promo','Standard_H16m','Standard_H16m_Promo','Standard_H16r','Standard_H16r_Promo','Standard_H16mr','Standard_H16mr_Promo','Standard_M8-2ms','Standard_M8-4ms','Standard_M8ms','Standard_M16-4ms','Standard_M16-8ms','Standard_M16ms','Standard_M32-8ms','Standard_M32-16ms','Standard_M32ls','Standard_M32ms','Standard_M32ts','Standard_M64-16ms','Standard_M64-32ms','Standard_M64ls','Standard_M64ms','Standard_M64s','Standard_M128-32ms','Standard_M128-64ms','Standard_M128ms','Standard_M128s','Standard_M64','Standard_M64m','Standard_M128','Standard_M128m','Standard_ND6s','Standard_ND12s','Standard_ND24rs','Standard_ND24s','Standard_NC6s_v2','Standard_NC12s_v2','Standard_NC24rs_v2','Standard_NC24s_v2','Standard_DC2s','Standard_DC4s','Standard_A8','Standard_A9','Standard_A10','Standard_A11'
]

for x in restricted:
    session.RemoveAttributeRestrictedValues(
        removeAttributeRestrictionRequests=[api.RemoveRestrictionRequest(
            FamilyName='Deployment Options',
            ModelName='Azure VM From Custom Image',
            Attributes=[api.Attribute(Name='VM Size', RestrictedValue=x)],
        )]
    )


# for x in restricted:
#     session.AddAttributeRestrictedValues([api.AddRestrictionRequest(
#         FamilyName='Deployment Options',
#         ModelName='Azure VM From Custom Image',
#         Attributes=[api.Attribute(Name='VM Size', RestrictedValue=x)],
#         Alphabetic='true'
#     )])

pass