
import streamlit as st ;
import requests
from PIL import Image 

avatar_img =  Image.open('3d avatar.gif');
image = Image.open('orchestrate.gif')
diwali_img = Image.open('DiwaliSales.jpg')
ecommerce_image = Image.open('ecommerce.jpeg')
emp_salary = Image.open('empSalary.jfif');
youtube_web_scrap = Image.open('YoutWebScrappingProject.jpg')
streamlit_datset_loader = Image.open('streamlit_datasetloader.jfif')
streamlit_data_visualization = Image.open('streamlit_python_visualizer.jfif')
imdb = Image.open('ImdbdataAnalysisProject.png')
udemy = Image.open('udemy.jpg')
titanic = Image.open('titanic.jfif')
student=Image.open('student.jpg')
googlePlaystore=Image.open('google.jfif')
adultsIncome = Image.open('adults_Income.jfif');
ecommerce = Image.open('ecommerce.jpeg')
youtube_ = Image.open('youtbe.jfif')

st.set_page_config(layout="wide");
st.subheader('Hello everyone, my name is Rishabh Shukla and I am very happy to meet you all! 😊');
st.title("Aspiring Business Analyst Eager to Drive Data-Driven Success");
st.write('''Hello👋, I'm Rishabh Shukla, a dedicated and results-driven Business Analyst. With a strong analytical mindset and a passion for problem-solving, I turn complex data into actionable insights. I can analyze business processes, identify opportunities for improvement, and delivering data-driven recommendations to drive growth and efficiency. I thrive on collaborating with cross-functional teams to achieve strategic goals. Let's work together to unlock the potential of your business.''');

with st.container():
    col1, col2, col3 = st.columns(3)

    # Define the buttons in the columns
    selected = 'About'
    if col1.button('About', key='about_button'):
        selected = 'About'
    if col2.button("Projects", key='projects_button'):
        selected = "Projects"
    if col3.button("Contact", key='contact_button'):
        selected = "Contact"

    # Apply background color to the buttons
    st.markdown(
        """
        <style>
        .streamlit-button {
            background-color: #007ACC;
            color: #FFFFFF;
            font-weight: bold;
            text-align: center;
        }
        .streamlit-button:hover {
            background-color: #005B9C;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


if selected == 'About':
        # Create two vertical columns
# Create two vertical columns
        st.subheader('Skill Sets')
        col3, col4 = st.columns(2)
        with col3:
         st.subheader('Technical Skills')
         st.write('''
         - Python 🐍
         - SQL 
         - PowerBI
         - JIRA
         - Excel
         - AI Prompting
         - Python Libraries: Pandas🐼, NumPy🔢, Matplotlib📊, Seaborn📈
         ''')
        with col4:
         st.subheader('Soft Skills')
         st.write('''
            - Communication👋
            - Adpatability😎
            - Teamwork 😄
            - Time Mangement⌛
            ''')
  
        col5,col6 = st.columns(2)
        with col5:
            st.subheader(''' 
        Education 
        - IISE COLLEGE
                         -Bachelor of Computer Application
                         -Grade : 77.9%
        - B.S.S Education Center
                         -PCB
                         -Percentage = 82%
        - B.S.S Education Center
                         Xth Percentage = 82%
        ''')
        with col6:
             st.image("https://giphy.com/embed/2hw8p8TpG8CgvuQOCT")
        col7,col8 = st.columns(2)
        with col5:
            st.subheader(''' 
                        Experience
                        - Fresher''')

if selected == 'Projects':
    st.header('My Projects')
    with st.container():
        st.write('##')
        col5,col6 = st.columns((1,2))
        with col5:
            st.image(streamlit_data_visualization);
        with col6:
            st.subheader('Python Streamlit Data Visualization Project');
            st.write("In this project we have build  Python Interactive Dashboard  using Streamlit and Plotly just like PowerBI and Tableau . Streamlit is a popular Python library used for building interactive web applications and dashboards. It simplifies the process of creating data-driven applications by providing a straightforward and intuitive interface. Here are some key uses of Streamlit in Python dashboards")
            st.write('[Github-link](https://github.com/aatmanrishi/Ecommerce-Store-Data-Visualization-Project.git)');
    with st.container():
        st.write('##')
        col7,col8 = st.columns((1,2))
        with col7:
            st.image(streamlit_datset_loader);
        with col8:
            st.subheader('Streamlit Dataset Loader');
            st.write("Here we have build a dataset uploader where we can upload our datset and see the overstatics of dataset . Get the overall info of dataset. Can drop rows which contain null values along with we can also drop duplicate items.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/StreamLitDataAnlayticsProject.git)');
    with st.container():
        st.write('##')
        col9,col10 = st.columns((1,2))
        with col9:
            st.image(udemy);
        with col10:
            st.subheader('Udemy Dataset Analysis');
            st.write("Here we have got Udemy dataset having different courses. Here we have found the total number of courses per subject.Most Popular course and top 10 most popular selling courses. We even got to know that how price effect the numerber of reviews. We found out that in which year highest number of courses were sold. We found the totat number of courses sell category wise per year .")
            st.markdown('[Github-link](https://github.com/aatmanrishi/Pandas-Exercises-.git)');
    with st.container():
        st.write('##')
        col11,col12 = st.columns((1,2))
        with col11:
            st.image(titanic);
        with col12:
            st.subheader('Titanic Dataset Analysis');
            st.write("We all know about famous titanic accident in which thousands of people lost there lives.We have got a dataset of passengers who were in Titanic at that time.Here we have found the no of people survived,about number of male and females .About the age of groups of people and many more.Here we performed tasks like dropping a column,handling missing vaues , data filtering and getting overall statistics about dataframe.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/Pandas-Exercises-.git)');
    with st.container():
        st.write('##')
        col11,col12 = st.columns((1,2))
        with col11:
            st.image(youtube_web_scrap);
        with col12:
            st.subheader('Youtube Web Scrapping');
            st.write(" Here, we build a Python Project to Scrape YouTube data using YouTube Data API. Using YouTube API, we extract the data and then load this data into a Python Pandas DataFrame and then analyze this data. Finally, we build simple visualization from this data using the Python Seaborn library.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/python_youtube_webscraping_project.git)');
    with st.container():
        st.write('##')
        col13,col14 = st.columns((1,2))
        with col13:
            st.image(imdb);
        with col14:
            st.subheader('IMDB Website Data Analysis');
            st.write(" Here we have done some questions for data analysis and data visualization from a very well-known real-world dataset. IMDB movie dataset.Here we have performed data cleaning and checked for duplicates . Find out which year has the highest voting, display number of movies per year and most popular movie with highest revenue.We have classified movies bases on Excellent,Good and Average .Find out about total number of action movies .Find out the unique value from Genre and many more.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/IMDwebScrappingProject.git)');
    with st.container():
        st.write('##')
        col15,col16 = st.columns((1,2))
        with col15:
            st.image(diwali_img);
        with col16:
            st.subheader('Diwali Sales Data Analysis');
            st.write("Here , we performed data analysis on Diwali Sales Dataset.Here we have got overall sataistics of our dataset . Performed Exploratory Data Analysis and Data Cleaning. It involved analyzing sales data related to Diwali, which is a significant holiday in many regions, and that the goal was to gain insights into sales patterns during this period.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/DiwaliAnalysisProject.git)');
    with st.container():
        st.write('##')
        col17,col18 = st.columns((1,2))
        with col17:
            st.image(emp_salary);
        with col18:
            st.subheader('Sanfrancisco Employee Salary Dataset Analysis');
            st.write("Here we have done data analysis on San Francisco City Employee Salaries. We have find out the differnt job title availble in city. Find out the maximum ,minimum and average base pay employees getting.Replace Nan with Not provided . Also Find about employee having highest basepay. Along with this we find out the average base of an employee year wise and also as per job title.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/Pandas-Exercises-.git)');
    with st.container():
        st.write('##')
        col19,col20 = st.columns((1,2))
        with col19:
            st.image(student);
        with col20:
            st.subheader('Student Result Analysis Project');
            st.write("Here ,we dive into the Student Result Analysis Project using Python, providing a fully practical demonstration. Here analyze student results efficiently and effectively using Python Enhance found the valuable insights into data analysis with this hands-on project.Here we'll see how education of parents effect the student .Here we get to know in which subject students phase most difficulty.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/Student_Result_Analysis.git)');
    with st.container():
        st.write('##')
        col21,col22 = st.columns((1,2))
        with col21:
            st.image(googlePlaystore);
        with col22:
            st.subheader('Google Play Store Dataset Analysis');
            st.write("Here we have got a Google play store dataset .From here we found about average rating of apps, total number of apps present. Find out the total number of paid and unpaid apps.Find that which category app are recieving highes rating . We get to know about the top apps having maximum installations . ")
            st.markdown('[Github-link](https://github.com/aatmanrishi/Pandas-Exercises-.git)');
    with st.container():
        st.write('##')
        col21,col22 = st.columns((1,2))
        with col21:
            st.image(ecommerce_image);
        with col22:
            st.subheader('Ecommerce Purchase Analysis');
            st.write("In this project we have worked on a real-world dataset available on Kaggle.Here we have find out about highest and lowest price of customer,there average price,also find out there ip adresses .We get to know that how many people have done purchase above 50,000. Along with this we get to know which are top 5 most popular email providers.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/Pandas-Exercises-.git)');
    with st.container():
        st.write('##')
        col23,col24 = st.columns((1,2))
        with col21:
            st.image(adultsIncome);
        with col22:
            st.subheader('Adults Income Analysis');
            st.write("In this project we have worked on Adults income analysis that we got form Kaggle.Here we have perform tasks like data cleaning and data manipulation . Along with Univariate Analysis and Bivariate Analysis.We also foud out that who has better chance to get salary greater than 50k Male or Female.Along with this we also found out that which working class has highest Salary. How many Persons haiving Bachelors and Masters Degree.")
            st.markdown('[Github-link](https://github.com/aatmanrishi/Pandas-Exercises-.git)');
    with st.container():
        st.write('##')
        col24,col25 = st.columns((1,2))
        with col24:
            st.image(youtube_);
        with col25:
            st.subheader('Youtube Data Anlaytics Project');
            st.write("Here we have data analysis on Youtube dataset that we got from Kaggle. Here we perform data cleaning , dropped rows with null values .Found out about the youtube channels with highest number of subscribers alon with this about youtube video having highest number of views along with this average on a regular youtube video . We also find out about the youtube video with maximum number of uploads .")
            st.markdown('[Github-link](https://github.com/aatmanrishi/Pandas-Exercises-.git)');

if selected == 'Contact':
    st.header('Get in touch with me')
    with st.container():
        st.write('###')
        col_x, _, col_y, _ = st.columns((1, 0.5, 2, 1))
        
        # Apply CSS to center col_x and col_y
        st.markdown('<style>div.css-1lrrx2m{margin: 0 auto; text-align: center;}</style>', unsafe_allow_html=True)
        
        with col_x:
            st.markdown('<div style="width:100%;height:0;padding-bottom:100%;position:relative;">'
                        '<iframe src="https://giphy.com/embed/daIfTnwGeY0J3zc1tg" width="100%" height="100%" '
                        'style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
                        '</div><p><a href="https://giphy.com/stickers/AnalyzeMedia-talk-lets-analyzemedia-daIfTnwGeY0J3zc1tg">'
                        'via GIPHY</a></p>', unsafe_allow_html=True)
        with col_y:
            st.subheader('Contact Information 📞')
            st.write("You can reach out to me via the following contact information:")
            st.write("- Email 📩: itzrrrrishabh@gmail.com")
            st.write("- LinkedIn: [Rishabh Shukla's LinkedIn](https://www.linkedin.com/in/rishabh-shukla-89123b254)")
            st.write("- Phone Number 📴 : 9653051157")
            st.write("- Address 🏡 : 109/274, R.K. Nagar, Kanpur")

