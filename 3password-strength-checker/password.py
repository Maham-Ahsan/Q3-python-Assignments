import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔑 Password Strength Checker")
st.markdown("""
## Welcome to the Password Strength Checker!🔐

This tool helps you evaluate the strength of your passwords and provides recommendations for improvement. 
Enter your password below to check its strength.
""")

password = st.text_input("Enter Your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score +=1
    else :
        feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌password should contain both upper and lower case characters.")

    if re.search(r'\d', password):
        score += 1
    else :
        feedback.append("❌password should contain at least one digit.")

    if re.search(r'[!@#$%&*+]', password):
         score += 1
    else:
        feedback.append("❌password should contain at least one special character(!@#$%&*+)")
    if score == 4:
        feedback.append("💹Your password is strong!🎉")
    elif score == 3:
        feedback.append("🟨Your password is medium strength. It could be strong.")
    else:
        feedback.append("🟥Your password is weak. It could be strong.")

    if feedback:
        st.markdown("## Improvement suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please! Enter Your password..")


    st.divider()
    st.markdown(
        """
    <div style='text-align:center;'>
         <p>Password strength checker..</p>
         <p>Build with ❤️ by <a href='https://github.com/Maham-Ahsan'>Maham Ahsan</a>using streamlit</p>
         </div>
    """,
           unsafe_allow_html=True
    )