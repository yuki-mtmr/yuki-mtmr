#!/usr/bin/env python3
"""
GitHubプロファイルREADME生成スクリプト

profile-config.yamlの設定に基づいてREADME.mdを生成する。
"""

import os
from pathlib import Path
from urllib.parse import quote

import yaml
from jinja2 import Environment, FileSystemLoader

from src.github_stats import fetch_user_stats, fetch_contributions, format_stats_for_display


def load_config(config_path: Path) -> dict:
    """
    YAMLファイルから設定を読み込む。

    Args:
        config_path: 設定ファイルのパス

    Returns:
        設定辞書
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def create_jinja_env(template_dir: Path) -> Environment:
    """
    Jinja2環境を作成する。

    Args:
        template_dir: テンプレートディレクトリのパス

    Returns:
        Jinja2 Environment
    """
    env = Environment(
        loader=FileSystemLoader(template_dir),
        keep_trailing_newline=True
    )
    # URLエンコード用フィルタを追加
    env.filters['urlencode'] = lambda s: quote(str(s), safe='')
    return env


def get_github_stats(username: str) -> dict:
    """
    GitHub APIから統計データを取得してフォーマットする。

    Args:
        username: GitHubユーザー名

    Returns:
        フォーマット済み統計データの辞書
    """
    user_stats = fetch_user_stats(username)
    contributions = fetch_contributions(username)

    stats = {
        'public_repos': user_stats.get('public_repos', 0),
        'followers': user_stats.get('followers', 0),
        'following': user_stats.get('following', 0),
        'contributions': contributions
    }

    formatted = format_stats_for_display(stats)
    return formatted


def generate_readme(config: dict, env: Environment) -> str:
    """
    設定に基づいてREADMEを生成する。

    Args:
        config: 設定辞書
        env: Jinja2環境

    Returns:
        生成されたREADME文字列
    """
    template = env.get_template('template.md')
    return template.render(**config)


def main():
    """メイン処理"""
    # パスの設定
    project_root = Path(__file__).parent.parent
    config_path = project_root / 'profile-config.yaml'
    template_dir = project_root / 'src'
    output_path = project_root / 'README.md'

    # 設定読み込み
    print(f'設定ファイルを読み込み中: {config_path}')
    config = load_config(config_path)

    # GitHub統計を取得
    username = config['user']['github_username']
    print(f'GitHub統計を取得中: {username}')
    config['github_stats'] = get_github_stats(username)

    # Jinja2環境作成
    env = create_jinja_env(template_dir)

    # README生成
    print('README.mdを生成中...')
    readme_content = generate_readme(config, env)

    # ファイル出力
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f'README.mdを生成しました: {output_path}')


if __name__ == '__main__':
    main()
