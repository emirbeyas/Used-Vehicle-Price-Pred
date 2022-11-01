#import arabamComDataSet
import Ilan
import arabamcomdataset.DbContext as DbContext
import csv


alinanHatalar = []
ilanLinkler = []
# while True:  
    
    # try:
    #     # arabamComDataSet.ilanLinkleriBul()

    # except:
    #     print("hi")
    # Ilan.ilanDetaylar(ilanLinkler)
    # print(str(len(ilanLinkler)))
    # for i in ilanLinkler:
    #     DbContext.addIlanLink(i)


with open('C:/Users/Emir/Desktop/AracimNeKadar/arabamcomdataset/ilanLinkler2.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    ilanLinkler = list(csv_reader)

# for i in list_of_csv:
#     # ilanLinkler.append(i[1])
#     print(i[0])
#     print(i[1])

# # # # ilanLinkler = DbContext.getIlanLink()

# # # # for i in range(5610):
# # # #     ilanLinkler.pop(0)

for i in ilanLinkler:
    try:
        print(i[0])
        Ilan.ilanDetaylar(i[1])
    except:
        alinanHatalar.append(i)

print(alinanHatalar)

# for i in range( 249 ,len(ilanLinkler)):
    
#     Ilan.ilanDetaylar(str(ilanLinkler[i]))

# for i in alinanHatalar:
#     print(i)

    # if input( str(len(DbContext.getAdvertList())) + ' Adet ilan var Devam Etmek Ister misiniz? (Y/N) : ') != 'Y':
    #     break
