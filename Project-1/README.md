# **Automate the Blogging at Jijeevisha**  

![Project Header](../assets/img/featured.png)  

## **Intro**  

#### Generate the Blog's Directory from Raw Data  
_(it can either be provided as user input or through some datafile)_  

**Detail:**  
We aim to create a `python` script to generate a [`markdown`](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf) file for the new blogs based on the user input. This `markdown` ([`index.md`](../jjv_template/blogs.txt)) is automatically rendered into a web page from the backend code. The program is meant to ask questions based on the required fields for the blog and populate the template file.  

For every blog, there is a directory that is named after the _'title of blog'_, and holds the following file(s):  
> 1. **`index.md`**: the original blogs' content  
> 2. **`featured.jpg`**: an _(optional)_ image for being displayed at the top of the blog  
> 3. Hence, the structure becomes:  
> ```  
> 📁 `title_of_blog` (directory)  
> │  
> ├── 📄 `index.md`       
> │  
> └── 🖼️ `featured.jpg`  
> ```

The **primary goal** is only to save the updated template (markdown) file as `index.md` into it's parent directory.  


## Approach  

Majorly the work is divided in 3-stages as below:  

> 📌 Basic **data file handling** to generate the blog's page based on the inputs  
> 📌 **Refining the blog's content** and extracting necessary information  
> 📌 Adding **image(s)** to our blog and uploading it to the website  

Preferably, this complete work is to be done in `python` and `bash` scripts. An initial level `python notebook` can be accessed [here](https://colab.research.google.com/github/jijeevisha-org/tech-front-info/blob/main/Project-1/blogGenerator.ipynb), which can be edited in the desired.  

---  

_🔗 Visit [https://jijeevishaorg.gitlab.io/](https://jijeevishaorg.ml/categories/) to know about Jijeevisha._  


