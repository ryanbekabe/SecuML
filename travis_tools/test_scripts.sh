#!/bin/bash

set -e

function experiments {
    SecuML_features_analysis Gaussians test
    SecuML_projection Gaussians test -a ground_truth.csv Lda
    SecuML_clustering Gaussians test Kmeans
    SecuML_DIADEM Gaussians test LogisticRegression -a ground_truth.csv
    SecuML_ILAB Gaussians test Random --auto
    SecuML_rm_project_exp --exp-id 1
    SecuML_rm_project_exp --project Gaussians
}

SECUMLCONF=conf/travis_psql.yml experiments
SECUMLCONF=conf/travis_mysql.yml experiments
