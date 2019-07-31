import create_CS_user

UC = create_CS_user.userCreator()
UC.add_external_user(
    username='a1234',
    password='123',
    email='a@b.com'
)
