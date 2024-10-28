# projectMapper_v1
 
This is a repository for a GUI based application for topic modelling and text search for research project dissertations.  

This is work developed by <b> Eduardo Viegas </b> and <b> Samuel Evans </b> at KCL.   The application is designed to make topic modelling accessible to others.  The purpose is to make it easy to analyse a large corpus of student research dissertations to extract themes and to search for key terms.  Whilst designed for that pupose it can be used to analyse any text.

The GUI interface is written in Tkinter and allows a range of searching and topic modelling approaches that include Latent Dirichlet Allocation using a Bayesian Optimisation search and Hierchical Dirichlet Process implemented via Gensim.

<br>

<p align="center">
  <img src="GUI_overview.png" width="300" >
</p>

The toolbox produces interactive visualisations of topics using pyLDAvis.

<p align="center">
  <img src="Visualisation.png" width="700" >
</p>

Thank you to Gensim: https://github.com/piskvorky/gensim and pyLDAvis: https://github.com/bmabey/pyLDAvis for implementations of topic modelling and visualisation tools.

