# Emotion Detection In Persian Texts     😡😀🙁😱😲😒🤐

In this project the goal was to classify Persian texts into 7 emotion categories: `ANGRY`, `HAPPY`, `SAD`, `FEAR`, `SURPRISE`, `HATE`, and `OTHER`.
and evaluate how well the model generalizes to unseen data.
So this project contains both DeepLearning & NLP techniques.

**P.S** : As you can see, there are two folders in my project. One of them is named `accuracy 60%`, which contains a different training dataset. However, this dataset has fewer emotion categories compared to the main dataset (`~50–53% accuracy`). I included it to test how a fixed model would perform when trained on a different dataset.

<p align="center">
<img src="img/Screenshot%202025-08-04%20at%2020.00.25.png" width="650"/>
</p>

# Data
* I used `.tsv` file and add 2 difference label, one of them is `Text` and other one is `Emotion`.
* Preprocessing included:
	*  Tokenization and normalization with **Hazm**.
	* Removing extra characters and cleaning texts.
	* Encode labels for best performance by using **Label Encoder**.
	* Handling class imbalance with **SMOTE**.
	* Use  **LIME** for model explanation.
	* Used **Tkinter** to display the final results in a UI form.

# Models

### Traditional ML Models:
* **Logistic Regression**, **SVM**, **Decision Tree**, **Random Forest**.
*  Vectorized input by using **TF-IDF**.
* **Best accuracy** achieved: 46%

### Deep Learning (LSTM)
* Used **Keras** with embedding layer initialized by FastText.
* Architecture: `Embedding -> SpatialDropout -> Bidirectional LSTM -> Dense`
* Loss: `Categorical Crossentropy`
* Optimizer: `Adam`
* EarlyStopping added for generalization.
**Best accuracy** achieved: 53%

<p align="center">
<img src="img/Screenshot%202025-08-04%20at%2020.19.48.png" width="650"/>
</p>


# NLP Pipeline
`Preprocessing ->  Vectorization -> Modeling -> Evaluation -> Visualization.`

# Run Detection App

To run the mini app, use the following command:

```bash
cd accuracy-50%
```
then:
```bash
python app.py
```


<p align="center">
  <img src="img/Screenshot%202025-08-04%20at%2001.26.59.png" width="500" />
</p>


# Final Words
Based on the official paper for this dataset, the maximum reported accuracy is around 70%. So, there are still other ways to improve the accuracy of my model, such as using  `Persian BERT model` like `HooshvareLab/bert-fa-base-uncased`.


