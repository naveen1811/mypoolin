from mypoolin.settings import deploy_url, CLIENT_ID

gplus_url = "https://accounts.google.com/o/oauth2/auth?redirect_uri="+\
                                                "{0}/mail/get_google_login/".format(deploy_url)+\
                                               "&response_type=code&client_id="+\
                                               "{0}".format(CLIENT_ID)+\
                                               "&scope=https://www.googleapis.com/auth/userinfo.email "+\
                                               "https://www.googleapis.com/auth/contacts"
