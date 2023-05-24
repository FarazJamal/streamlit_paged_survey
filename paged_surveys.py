import streamlit as st
import pandas as pd
import base64

page_options = [
    ["ALFA ROMEO", "ASTON MARTIN", "AUDI", "BMW"],
    ["CHEVROLET", "DODGE", "FERRARI", "HONDA"],
    ["JAGUAR", "LAMBORGHINI", "MAZDA", "MCLAREN"],
    ["MERCEDES-BENZ", "NISSAN", "PAGANI AUTOMOBILI S.P.A", "PORSCHE"],
    ["FIAT", "MINI", "SCION", "SUBARU"],
    ["BENTLEY", "BUICK", "FORD", "HYUNDAI"],
    ["LEXUS", "MASERATI", "ROUSH", "VOLKSWAGEN"],
    ["ACURA", "CADILLAC", "INFINITI", "KIA"],
    ["MITSUBISHI", "ROLLS-ROYCE", "TOYOTA", "VOLVO"],
    ["CHRYSLER", "LINCOLN", "GMC", "RAM"]

]

selected_options = st.session_state.get("selected_options", [[] for _ in page_options])

def main():
    st.set_page_config(page_title="Radio Selection App")
    page_index = st.session_state.get("page_index", 0)
    num_pages = len(page_options)
    page_title = f"Page {page_index + 1} of {num_pages}"
    radio_options = page_options[page_index]
    st.write(page_title)
    selected_option = st.radio("Select an option:", radio_options)

    for i in range(num_pages):
        if selected_option in page_options[i]:
            selected_options[page_index] = selected_option
            st.session_state["selected_options"] = selected_options

    if page_index > 0:
        if st.button("Previous"):
            st.session_state["page_index"] = page_index - 1
            st.experimental_rerun()

    if page_index < num_pages - 1:
        if st.button("Next"):
            st.session_state["page_index"] = page_index + 1
            st.experimental_rerun()

    if page_index == num_pages - 1:
        if st.button("Submit"):
            df = pd.DataFrame(selected_options).transpose()
            df.columns = [f"Option {i+1}" for i in range(num_pages)]
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="selected_options.csv">Download CSV</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
