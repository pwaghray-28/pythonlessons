import dropbox
class Dbstransfer:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file1,file2):
        d = dropbox.Dropbox(self.access_token)
        f = open(file1,'rb')
        d.files_upload(f.read(),file2)
def main():
    access_token = 'sl.AwjdNe_14xm8e4z0ktv9_eIWnDaEOvGngZQXgQye_2T3L4jgEQQqfJyvT0MdUiFuz5GPZdyh2zacs3ZiBiAQBgDOzo2kowmo5I405hqDi0u-081hzOtdOuDl7OZcT5XKNPOPXrg'
    transfer = Dbstransfer(access_token)
    file1 = input("Enter the file you want to transfer")
    file2 = input("Enter the name for storage")
    transfer.upload_file(file1,file2)
    print("File is moved")
main()