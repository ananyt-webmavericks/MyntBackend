"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index
from django.conf import settings
from django.conf.urls.static import static 

 
 
urlpatterns = [
    path('', index,name="index"),
    path('admin/', admin.site.urls),
    path('',include('MT_User.urls')),
    path('',include('MT_Investor_Kyc.urls')),
    path('',include('MT_Investor_Payment.urls')),
    path('',include('MT_Investor_Choose_Sector.urls')),
    path('',include('MT_Investor_Verify_Standards.urls')),
    path('',include('MT_Investor_Verifiy_Nationality.urls')),
    path('',include('MT_Raise.urls')),
    path('',include('MT_Startup_Agreements.urls')),
    path('',include('MT_Startup_Banner_Dets.urls')),
    path('',include('MT_Startup_FAQs_Dets.urls')),
    path('',include('MT_Startup_Investors_Dets.urls')),
    path('',include('MT_Startup_Teaminfo.urls')),
    path('',include('MT_Startup_Pressinfo.urls')),
    path('',include('MT_Startup_Pitchinfo.urls')),
    path('',include('MT_Startup_Companyinfo.urls')),
    path('',include('MT_Startup_Analystics_TRinfo.urls')),
    path('',include('MT_Startup_Pitch_Visioninfo.urls')),
    path('',include('MT_Startup_Pitch_Usagefundsinfo.urls')),
    path('',include('MT_Startup_Pitch_Tractioninfo.urls')),
    path('',include('MT_Startup_Pitch_Solution.urls')),
    path('',include('MT_Startup_Pitch_Businfo.urls')),
    path('',include('MT_Startup_Pitch_Productinfo.urls')),
    path('',include('MT_Startup_Pitch_Probleminfo.urls')),
    path('',include('MT_Startup_Pitch_Customerinfo.urls')),
    path('',include('MT_Startup_Pitch_Competitioninfo.urls')),
    path('',include('MT_Startup_Pitch_PotentialReturnsinfo.urls')),
    path('',include('Campaign_Banner.urls')),
    path('',include('Campaign_Press.urls')),
    path('',include('Campaign_Investors.urls')),
    path('',include('Campaign_FAQs.urls')),
    path('',include('E_sign.urls')),
    path('',include('Campaign_Analystics.urls'))
    
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
