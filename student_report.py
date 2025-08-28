import streamlit as st

# ---------- Functions ----------
def validate_student_number(sno):
    return sno.isdigit() and int(sno) in range(100, 200)

def validate_student_name(name):
    words = name.split()
    jname = "".join(words)
    return jname.isalpha()

def validate_marks(marks):
    return marks.isdigit() and int(marks) in range(0, 101)

def calculate_grade(c, cpp, py):
    totmarks = c + cpp + py
    percent = (totmarks / 300) * 100

    if c < 40 or cpp < 40 or py < 40:
        grade = "FAIL"
    elif totmarks in range(250, 301):
        grade = "DISTINCTION"
    elif totmarks in range(200, 250):
        grade = "FIRST"
    elif totmarks in range(150, 200):
        grade = "SECOND"
    elif totmarks in range(120, 150):
        grade = "THIRD"
    else:
        grade = "FAIL"

    return totmarks, percent, grade


# ---------- Streamlit UI ----------
st.title("🎓 Student Marks Report App")

sno = st.text_input("Enter Student Number (100-199):")
name = st.text_input("Enter Student Name:")

c_marks = st.text_input("Enter C Language Marks (0-100):")
cpp_marks = st.text_input("Enter C++ Language Marks (0-100):")
py_marks = st.text_input("Enter Python Language Marks (0-100):")

if st.button("Generate Report"):
    # Validation
    if not validate_student_number(sno):
        st.error("❌ Invalid Student Number! Must be between 100-199.")
    elif not validate_student_name(name):
        st.error("❌ Invalid Name! Only alphabets allowed.")
    elif not validate_marks(c_marks) or not validate_marks(cpp_marks) or not validate_marks(py_marks):
        st.error("❌ Invalid Marks! Enter numbers between 0-100.")
    else:
        # Convert marks
        c = int(c_marks)
        cpp = int(cpp_marks)
        py = int(py_marks)

        totmarks, percent, grade = calculate_grade(c, cpp, py)

        st.success("✅ Report Generated Successfully!")

        # Show Report
        st.subheader("📑 Student Marks Report")
        st.write(f"**Student Number:** {sno}")
        st.write(f"**Student Name:** {name}")
        st.write(f"**Marks in C:** {c}")
        st.write(f"**Marks in C++:** {cpp}")
        st.write(f"**Marks in Python:** {py}")
        st.write(f"**Total Marks:** {totmarks}")
        st.write(f"**Percentage:** {round(percent, 2)}%")
        st.write(f"**Grade:** {grade}")
