import pickle
import streamlit as st
import numpy as np
import pandas as pd
# Load the trained model
loaded_model = pickle.load(open("C:/Users/sagar/Desktop/Terror attack prediction/trained_model.pkl", 'rb'))
feature_cols = ['Associates','injured','deceased','arrests','atcktype_arson',
                'atcktype_assassination','atcktype_bombing','atcktype_hijacking',
                'atcktype_shooting','atcktype_stabbing','targetT_civilians','targetT_infrastructure',
                'targetT_police','targetT_tourists','targetT_government officials','weapon_bladed weapons',
                'weapon_chemical','weapon_explosives','weapon_firearms','weapon_incendiary','weapon_melee',
                'iqtip_no','iqtip_unknown','iqtip_yes','Motive_ethnic','Motive_religious','Motive_political',
                'fundings_international','fundings_local','fundings_unknown']



# Function to make predictions
def predict_attack_type(input_data):
    
    # Make predictions
    prediction = loaded_model.predict(input_data)
    
    if prediction[0] == 1:
        return 'Major Attack'
    else:
        return 'Minor Attack'

# Main Streamlit app
def main():
    # Set a title for your app
    st.title('Terrorist Attack Prediction')

    # Provide instructions to the user
    st.markdown("Select the relevant features to predict whether the attack is major or minor:")
    # motive,funding
    # Create checkboxes for root features
    col1, col2 = st.columns(2)
    associates = col1.number_input('Associates',min_value=0)
    injured = col2.number_input('Injured', min_value=0)

    col3, col4 = st.columns(2)
    deceased = col3.number_input('Deceased', min_value=0)
    arrests = col4.number_input('Arrests',min_value=0)
        
    col5, col6 = st.columns(2)
    attack_type = col5.selectbox('Attack Type', ['Arson', 'Assassination', 'Bombing', 'Hijacking', 'Shooting', 'Stabbing'])
    target_type = col6.selectbox('Target Type', ['Civilians', 'Infrastructure', 'Police', 'Tourists', 'Government Officials'])
        
    col7,col8 = st.columns(2)
    weapon = col7.selectbox('Weapon Type', ['Bladed Weapons', 'Chemical', 'Explosives', 'Firearms', 'Incendiary', 'Melee'])
    iqtp = col8.selectbox('Intelligence Tip', ['No', 'Unknown', 'Yes'])
    
    col9,col10 = st.columns(2)
    motive = col9.selectbox('Motive',['Ethnic', 'Religious', 'Political'])
    funding = col10.selectbox('Funding', ['International', 'Local', 'Unknown'])

    input_feature = {'Associates':[associates],'injured':[injured],'deceased':[deceased],'arrests':[arrests],
                     'atcktype_arson':[1 if attack_type == 'Arson' else 0],'atcktype_assassination':[1 if attack_type == 'Assassination' else 0],
                        'atcktype_bombing':[1 if attack_type == 'Bombing' else 0],'atcktype_hijacking':[1 if attack_type == 'Hijacking' else 0],
                        'atcktype_shooting':[1 if attack_type == 'Shooting' else 0],'atcktype_stabbing':[1 if attack_type == 'Stabbing' else 0],
                        'targetT_civilians':[1 if target_type == 'Civilians' else 0],'targetT_infrastructure':[1 if target_type == 'Infrastructure' else 0],
                        'targetT_police':[1 if target_type == 'Police' else 0],'targetT_tourists':[1 if target_type == 'Tourists' else 0],
                        'targetT_government officials':[1 if target_type == 'Government Officials' else 0],'weapon_bladed weapons':[1 if weapon == 'Bladed Weapons' else 0],
                        'weapon_chemical':[1 if weapon == 'Chemical' else 0],'weapon_explosives':[1 if weapon == 'Explosives' else 0],
                        'weapon_firearms':[1 if weapon == 'Firearms' else 0],'weapon_incendiary':[1 if weapon == 'Incendiary' else 0],
                        'weapon_melee':[1 if weapon == 'Melee' else 0],'iqtip_no':[1 if iqtp == 'No' else 0],
                        'iqtip_unknown':[1 if iqtp == 'Unknown' else 0],'iqtip_yes':[1 if iqtp == 'Yes' else 0],
                        'Motive_ethnic':[1 if motive == 'Ethnic' else 0],'Motive_religious':[1 if motive == 'Religious' else 0],
                        'Motive_political':[1 if motive == 'Political' else 0],'fundings_international':[1 if funding == 'International' else 0],
                        'fundings_local':[1 if funding == 'Local' else 0],'fundings_unknown':[1 if funding == 'Unknown' else 0]}
    input_feature = pd.DataFrame(input_feature)

    if st.button('Predict'):
        prediction = predict_attack_type(input_feature)
        st.success(f"Prediction: The Attack will be {prediction}", icon="🎉")
    # Perform Prediction
if __name__ == '__main__':
    main()