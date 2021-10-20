# What affects the most in the price of a notebook?

In addition to the purchase and sale of each component. We would like to know wich one affects the most when the price is fixed.

We did an statistical analysis and got some few results.

## Requirements

The Python Notebook was written using a Python Google Colab Notebook environment, and the following libraries:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [Matplotlib](http://matplotlib.org/)
- [Scikit-Learn](http://scikit-learn.org/stable/)
- [Scipy](https://www.scipy.org/)
- [Statmodels](https://www.statsmodels.org/stable/index.html)
- [Patsy](https://pypi.org/project/patsy/)


## Dataset

The data was scraped from the [notebooks section](https://www.solotodo.cl/notebooks) of the [Solotodo Website](https://www.solotodo.cl/), using 

- [scrapy](https://scrapy.org/)

To get the dataset, inside the **nbscraper** folder, on the terminal run:

```
scrapy crawl notebooks -O notebooks.csv
```


## Results

We got the importances of each notebook component, and the respective error.


## Things to be done

- [X] Verify the statistical analysis using Classical Machine Learning models.
- [X] Improve the predictive power with an hyperparameter search.
- [X] Neural Network Added to test the predictive power.


## Support

Give a :star: if you like it :hugs:.