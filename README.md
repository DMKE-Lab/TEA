## Implementation of Open Entity Alignment (Open-EA)

Paper: Embedding-based Entity Alignment between Multi-source Temporal Knowledge Graphs(TEA)



This repository contains the implementation of the TEA architectures described in the paper.

## Installation
* Python 3.x (tested on Python 3.6)
* Tensorflow 1.x (tested on Tensorflow 1.8 and 1.12)
* Scipy
* Numpy
* Graph-tool or igraph or NetworkX
* Pandas
* Scikit-learn
* Matching==0.1.1
* Gensim

We recommend creating a new conda environment to install and run OpenEA. You should first install tensorflow-gpu (tested on 1.8 and 1.12), graph-tool (tested on 2.27 and 2.29,  the latest version would cause a bug), and python-igraph using conda:

```bash
conda create -n openea python=3.6
conda activate openea
conda install tensorflow-gpu==1.12
conda install -c conda-forge graph-tool==2.29
conda install -c conda-forge python-igraph
```

## Package Description
```
run/
├── openea/
│   ├── approaches/: package of the implementations for existing embedding-based entity alignment approaches
│   ├── models/: package of the implementations for unexplored relationship embedding models
│   ├── modules/: package of the implementations for the framework of embedding module, alignment module, and their interaction
│   ├── expriment/: package of the implementations for evalution methods
```

## Datasets
We choose three well-known KGs as our sources: DBpedia (2016-10),Wikidata (20160801) and YAGO3. Also, we follow the conventions in JAPE to generate datasets of two sizes with 15K and 100K entities, using the IDS algorithm. Besides, we generate two versions of datasets for each pair of KGs to be aligned. S is generated by directly using the IDS algorithm. For D, we first randomly delete entities with low degrees (d <= 5) in the source KG to make the average degree doubled, and then execute IDS to fit the new KG. The statistics of the datasets are shown below.  


|---------Types--------|Languages|Dataset names|

|-----------------------|----------|-------------------| 

|15K sparse datasets |English| DW15S, DY15S

|15K dense datasets | English | DW15D, DY15D

|100K sparse datasets| English | DW100S, DY100S

|100K dense datasets| English | DW100D, DY100D

The  datasets can be downloaded from [Baidu Wangpan](https://pan.baidu.com/s/1mYec9tLp9tQpnqx0JsH7xw) (password: 85kq).

## Experiments

### Experiment Settings
The common hyper-parameters used for OpenEA are shown below.

<table style="text-align:center">
    <tr>
        <td style="text-align:center"></td>
        <th style="text-align:center">15K</th>
        <th style="text-align:center">100K</th>
    </tr>
    <tr>
        <td style="text-align:center">Batch size for rel. triples</td>
        <td style="text-align:center">5,000</td>
        <td style="text-align:center">20,000</td>
    </tr>
    <tr>
        <td style="text-align:center">Termination condition</td>
        <td style="text-align:center" colspan="2">Early stop when the Hits@1 score begins to drop on <br>
            the validation sets, checked every 10 epochs.</td>
    </tr>
    <tr>
        <td style="text-align:center">Max epochs</td>
        <td style="text-align:center" colspan="2">2,000</td>
    </tr>
</table>

Besides, it is well-recognized to split a dataset into training(20%), validation(10%) and test(70%) sets. 
We use Hits@m (m = 1, 5, 10), mean rank (MR) and mean reciprocal rank (MRR) as the evaluation metrics.  Higher Hits@m and MRR scores as well as lower MR scores indicate better performance.

### Train and Test
To run the off-the-shelf approaches on our datasets and reproduce our experiments, change into the ./run/ directory and use the following script:


```bash
python main_from_args.py "predefined_arguments" "dataset_name" "split"
```

For example, if you want to run TEA on DW15S, please execute the following script:
    
```bash
python main_from_args.py ./args/tea_args_15K.json DW15S 721/
```

