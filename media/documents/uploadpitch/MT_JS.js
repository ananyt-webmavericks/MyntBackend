input["companyinfoid"]
input["cicountry"]
input["cistate"]
input["cicity"]
input["cistate"] 
input["cipincode"]
input["ciaddress"]
input["ciCompanyWebsite"]
input["ciFacebookLink"]
input["ciInstagramLink"]
input["ciLinkedInLink"]
input["ciLegalName"]
input["ciCinNumber"]
input["ciDate"]
input["ciIncorporation"]
input["ciSector"]
input["ciAmountInvested"]
input["ciEmployees"]
this.setState({
    ID: response.data.ID,
    MTUSER_ID  :response.data.MTUSER_ID ,
    EMAIL : response.data.EMAIL,
    MODULE:response.data.MODULE,
    COUNTRY:response.data.COUNTRY,
    STATE:response.data.STATE,
    CITY:response.data.CITY,
    PINCODE:response.data.PINCODE,
    ADDRESS:response.data.ADDRESS,
    COMPANY_WEBSITE:response.data.COMPANY_WEBSITE,
    FB_LINK : response.data.FB_LINK,
    INSTA_LINK : response.data.INSTA_LINK,
    LINKEDIN_LINK : response.data.LINKEDIN_LINK,
    LEGAL_NAME:response.data.LEGAL_NAME,
    CIN_NUMBER:response.data.CIN_NUMBER,
    DATE_OF_INCORPORATATION:response.data.DATE_OF_INCORPORATATION,
    INCORPORATION_TYPE:response.data.INCORPORATION_TYPE,
    ABOUT_COMPANY:response.data.ABOUT_COMPANY,
    AMOUNT_INVESTED:response.data.AMOUNT_INVESTED,
    NO_OF_EMPLOYEES:response.data.NO_OF_EMPLOYEES,
    STATUS: response.data.STATUS,
    COMMENTS:response.data.COMMENTS,
    DESCRIPTION: response.data.DESCRIPTION,
    CREATED_USER: response.data.CREATED_USER,
    CREATED_DATE: response.data.CREATED_DATE,
    MODIFIED_USER: response.data.MODIFIED_USER,
    MODIFIED_DATE: response.data.MODIFIED_DATE,
    
  });  