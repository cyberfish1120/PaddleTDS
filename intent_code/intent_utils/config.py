# --- coding:utf-8 ---
# author: Cyberfish time:2021/7/19
import argparse


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--train_file', default='../data/intent_train.json')
    parser.add_argument('--test_file', default='../data/intent_test.json')

    parser.add_argument('--batch_size', default=512)
    parser.add_argument('--epoch', default=15)

    parser.add_argument('--seed', default=2021)
    parser.add_argument('--max_len', default=128)
    parser.add_argument('--lr', default=1e-5)

    return parser.parse_args()