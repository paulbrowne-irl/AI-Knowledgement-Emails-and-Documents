import streamlit as st
import pandas as pd

import util.rag_controller as rag_controller

import sidebar
from importlib import reload

#Window setup
st.title('Find Similar Clients')

#Fields on Sidebar
reload(sidebar)

#make sure setup gets run at start
rag_controller.setup()


#############
# Main UI

if 'num_docs' in locals():
    st.info(f' Showing {num_docs} matches on meaning, not text', icon="ℹ️")



with st.form('my_form'):
    input_text = st.text_area('Enter text:', 'Paste in *any* text that describes the starting client.\n\n I will find similar companies based on *meaning* not just keyword matching')
    
    num_docs = st.slider('How many similar clients / docs do you want to see?', 1, 50,5)
    submitted = st.form_submit_button('Submit')
    
     # Tabs setup
    tab_summary, tab_full = st.tabs(["Summary", "Full"])


    #check we need to generate check
    if submitted:
            
        # Find nearest match documents
        similar_docs = rag_controller.get_nearest_match_documents(sidebar.document_search, input_text)

        #setup empty dataframe for display
        nf= pd.DataFrame.from_dict({})


        with tab_summary:

            #convert
            for doc in similar_docs:
                #pd.DataFrame.from_dict(doc)
                
                nf = nf.append({'Name': doc.metadata.get("name"),
                                    'Page': doc.metadata.get("page"),
                                    'Type':doc.metadata.get("type"),
                                    'Product':doc.metadata.get("product")}
                                    , ignore_index=True)
        
            # use magic output
            nf
            
            with tab_full:

                # use magic output
                for doc in similar_docs:
                    #pd.DataFrame.from_dict(doc)
                    st.subheader(doc.metadata.get("name"))
                    doc.page_content
                  
     
   