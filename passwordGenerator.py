import streamlit as st
import re

# Set page config and title
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

# Custom CSS styling
st.markdown("""
    <style>
    @keyframes titleAnimation {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .animated-title {
        display: inline-block;
        animation: titleAnimation 2s ease-in-out infinite;
        background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% 200%;
        animation: titleAnimation 2s ease-in-out infinite, gradient 3s ease infinite;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        border: 2px solid #45a049;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .password-input {
        background-color: #f0f8ff;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
        border: 2px solid #4a90e2;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }
    .strength-meter {
        height: 10px;
        border-radius: 5px;
        margin: 1rem 0;
        transition: all 0.3s ease;
        border: 1px solid #ddd;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }
    .strength-container {
        background: #f0f0f0;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        border: 3px solid #6c63ff;
    }
    .strength-bar {
        height: 40px;
        background: linear-gradient(45deg, 
            #ff0000 0%,
            #ff4500 20%,
            #ffa500 40%,
            #ffff00 60%,
            #7cff00 80%,
            #00ff00 100%
        );
        border-radius: 20px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        border: 2px solid rgba(255,255,255,0.3);
        animation: gradient 3s ease infinite;
    }
    @keyframes gradient {
        0% {background-position: 0% 50%}
        50% {background-position: 100% 50%}
        100% {background-position: 0% 50%}
    }
    .strength-fill {
        height: 100%;
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(5px);
        transition: all 0.8s ease;
        border-right: 2px solid rgba(0,0,0,0.1);
    }
    .strength-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin: 15px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        background: linear-gradient(45deg, #ff0000, #00ff00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        border-bottom: 2px solid transparent;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .strength-emoji {
        font-size: 30px;
        margin: 10px 0;
        text-align: center;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<h1 class='animated-title'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)
st.write("Check how strong your password is!")

# Password input
password = st.text_input("Enter your password", type="password", key="password")

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
        feedback.append("✅ Length is good")
    else:
        feedback.append("❌ Password should be at least 8 characters")
        
    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✅ Contains uppercase")
    else:
        feedback.append("❌ Should contain uppercase letters")
        
    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains lowercase")
    else:
        feedback.append("❌ Should contain lowercase letters")
        
    # Number check
    if re.search(r"\d", password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Should contain numbers")
        
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Should contain special characters")
        
    return score, feedback

if password:
    strength, feedback = check_password_strength(password)
    
    # Display strength meter
    strength_percentage = (strength / 5) * 100
    
    # Emoji and text based on strength
    if strength_percentage <= 20:
        strength_text = "Very Weak"
        emoji = "😱"
    elif strength_percentage <= 40:
        strength_text = "Weak"
        emoji = "😟"
    elif strength_percentage <= 60:
        strength_text = "Medium"
        emoji = "😐"
    elif strength_percentage <= 80:
        strength_text = "Strong"
        emoji = "😊"
    else:
        strength_text = "Very Strong"
        emoji = "💪"
    
    # Display colorful animated strength meter
    st.markdown(f"""
        <div class="strength-container">
            <div class="strength-emoji">{emoji}</div>
            <div class="strength-bar">
                <div class="strength-fill" style="width: {100-strength_percentage}%;"></div>
            </div>
            <div class="strength-text">
                {strength_text} ({strength_percentage}%)
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Display feedback
    st.markdown("### Password Requirements:")
    for item in feedback:
        st.write(item)

# Password tips
st.markdown("---")
st.markdown("### Tips for a Strong Password:")
tips = """
- Use at least 8 characters
- Include uppercase and lowercase letters
- Include numbers
- Include special characters (!@#$%^&*)
- Avoid using personal information
- Don't use common words or patterns
"""
st.info(tips)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'><small>Created by Dilsher Khaskheli</small></div>", unsafe_allow_html=True)
