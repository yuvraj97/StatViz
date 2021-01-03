import patreon
def get_patreon_data():
    # print("fetching patreon API", flush=True)
    access_token = 'eCzADomkBdoFuXDee-6s8D259MVegJqoMuqxm8W2AWE'
    api_client = patreon.API(access_token)
    campaign_response = api_client.fetch_campaign()
    campaign_id = campaign_response.data()[0].id()

    # Fetch all pledges
    all_pledges = []
    cursor = None
    while True:
        pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25, cursor=cursor)
        all_pledges.extend(pledges_response.data())
        cursor = api_client.extract_cursor(pledges_response)
        if not cursor:
            break

    users = {}
    for pledge in all_pledges:
        email = pledge.relationship('patron').attribute('email')
        users[email] = pledge.attribute('amount_cents')
    return users
