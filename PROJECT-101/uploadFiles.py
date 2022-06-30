import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(),file_to)
def main():
    access_token ="sl.BKhO6XlEeMYSs1-Y1pTMjHpLZsn0qu_fD9ZSCofewmt71_mv3L-BYGHADbpT0fH6iUn1403AT1SgtG65i4DTn_Ftam3BXaRrBA1fri4yy7V90so5LfkuW8zNCdo-C5jCjRtZIR-hSbh-"           
    transferdata = TransferData(access_token)
    file_from = "test2.txt"
    file_to = "/Dropbox/test2.txt"
    transferdata.upload_file(file_from, file_to)
if __name__ == "__main__":
    main()    