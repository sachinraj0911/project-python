import win32com.client
import win32com

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
accounts = win32com.client.Dispatch("Outlook.Application").Session.Accounts;


for account in accounts:
    global inbox
    inbox = outlook.Folders(account.DeliveryStore.DisplayName)
    folders = inbox.Folders
    for folder in folders:
        if folder.name == "PingId":
            #print(folder)

