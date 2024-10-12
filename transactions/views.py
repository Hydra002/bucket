from datetime import datetime

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import tabula

from transactions.models import TxnCategory, Transactions


def get_uncommitted_transactions(request):



@csrf_exempt
def upload_report(request):
    if request.method == 'POST':
        files = request.FILES
        txn_category = request.POST.get("category")

        if len(files) != 0:
            uploaded_file = files['txns_report'].file
            path = default_storage.save('C:\\Users\\gurchars\\work\\projects\\bucket\\uploads\\temp-1.pdf', ContentFile(uploaded_file.read()))
            df = tabula.read_pdf(path, lattice=True)
            all_txns = df[0].values
            for txn in all_txns:
                txn[1] = txn[1].replace('/', '|')
                # txn[1] = txn[1].replace('\\', '|')
                txn[1] = txn[1].replace('\r', ' ')
    #           Save to DB
                print('Date: {0}  Description: {1}  Amount: {2}  Txn Type: {3}'.format(txn[0], txn[1], txn[2], txn[3]))

                category = TxnCategory.objects.filter(title=txn_category).first()
                txn_date = datetime.strptime(txn[0], "%d-%m-%Y")
                txn_type = "IN" if txn[3] == 'CR' else "EX"
                txn = Transactions(description = txn[1], date = txn_date, amount = int(txn[2]), txn_type = txn[3], category=category)
                txn.save()

    return HttpResponse("Upload Report API")