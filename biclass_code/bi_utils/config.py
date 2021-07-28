# --- coding:utf-8 ---
# author: Cyberfish time:2021/7/20
import argparse


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_file', default='../data/bi_train.json')
    parser.add_argument('--test_file', default='../data/bi_test.json')
    parser.add_argument('--seed', default=2021)
    parser.add_argument('--batch_size', default=64)
    parser.add_argument('--lr', default=1e-5)
    parser.add_argument('--epoch', default=10)
    parser.add_argument('--max_len', default=128)

    return parser.parse_args()