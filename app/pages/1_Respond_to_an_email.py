import app as app

from importlib import reload

import settings.config as config
import streamlit as st

import pages.support.app_sidebar as app_sidebar
import pages.support.page_support_outlook as page_support_outlook


import templates.prompts




#Window setup
st.title('Auto draft email responses :email:')

#Fields on Sidebar
reload(app_sidebar)

# Config Info we want to echo to the user
BREAK_AFTER_X_MAILS = config.read_int("BREAK_AFTER_X_MAILS")
MAILBOX_NAME = config.read("MAILBOX_NAME")
FOLDER_NAME = config.read("FOLDER_NAME")

st.markdown(f"Using mailbox account **{MAILBOX_NAME}**, subfolder **{FOLDER_NAME}**. Will pause after **{BREAK_AFTER_X_MAILS}** emails")


#############
# Main UI

with st.form('my_form'):
   


    # Tabs setup
    tab_mails, tab_test, tab_generate_draft = st.tabs([":email: Mails in Inbox", ":test_tube: Test run", ":checkered_flag: Generate Drafts"])


    with tab_mails:
        email_df = page_support_outlook.loop_through_outlook_emails(False)
        st.dataframe(data=email_df, width=3600)
        submitted_view = st.form_submit_button('Refresh View')


    with tab_test:
        email_df = page_support_outlook.loop_through_outlook_emails(True)
        st.dataframe(data=email_df, width=3600)
        submitted_teset = st.form_submit_button('Test Response')

    with tab_generate_draft:
        email_df = page_support_outlook.loop_through_outlook_emails(True, True)
        st.dataframe(data=email_df, width=3600)
        submitted_teset = st.form_submit_button('Generate Draft Emails')



    #send of form
   


  