from rest_framework import serializers 
from MT_Investor_Payment.models import PaymentModel
 
 
class PaymentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = PaymentModel
        fields = ("id",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "COMPANY_INVESTED_IN",
                  "INVESTED_DATE",
                  "INV_AMOUNT",
                  "INV_CONVENIENCE_FEE",
                  "INV_GST",
                  "INV_TOT",
                  "INV_CHK_AGREE_TERMS",
                  "INV_PAID",
                  "INV_BALANCE",
                  "AGREEMENT_FILE_DOC",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")