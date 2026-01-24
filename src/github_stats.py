"""
GitHub統計データ取得モジュール

GitHub APIを使用してユーザーの統計情報を取得する。
外部サービス（github-readme-stats等）に依存せず、
直接APIから取得してテキスト表示する。
"""
import re
from typing import Dict

import requests


def fetch_user_stats(username: str) -> Dict:
    """
    GitHub APIからユーザー統計を取得する。

    Args:
        username: GitHubユーザー名

    Returns:
        統計データの辞書（public_repos, followers, following等）
    """
    url = f'https://api.github.com/users/{username}'

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return _default_stats()

        data = response.json()
        return {
            'public_repos': data.get('public_repos', 0),
            'followers': data.get('followers', 0),
            'following': data.get('following', 0),
            'public_gists': data.get('public_gists', 0)
        }
    except requests.RequestException:
        return _default_stats()


def _default_stats() -> Dict:
    """デフォルトの統計データを返す"""
    return {
        'public_repos': 0,
        'followers': 0,
        'following': 0,
        'public_gists': 0
    }


def fetch_contributions(username: str) -> int:
    """
    GitHubのコントリビューション数を取得する。

    GitHubプロフィールページからコントリビューション数をスクレイピング。

    Args:
        username: GitHubユーザー名

    Returns:
        年間コントリビューション数
    """
    url = f'https://github.com/{username}'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        }
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return 0

        # コントリビューション数を正規表現で抽出
        # パターン1: "1,234 contributions in the last year"
        match = re.search(
            r'([\d,]+)\s+contributions?\s+in\s+the\s+last\s+year',
            response.text
        )
        if match:
            count_str = match.group(1).replace(',', '')
            return int(count_str)

        # パターン2: 新しいGitHub UIのパターン
        match = re.search(
            r'(\d[\d,]*)\s+contribution',
            response.text
        )
        if match:
            count_str = match.group(1).replace(',', '')
            return int(count_str)

        return 0
    except (requests.RequestException, ValueError):
        return 0


def format_stats_for_display(stats: Dict) -> Dict[str, str]:
    """
    統計データを表示用にフォーマットする。

    Args:
        stats: 統計データの辞書

    Returns:
        フォーマット済みの表示用辞書
    """
    return {
        'repos': f"{stats.get('public_repos', 0):,}",
        'followers': f"{stats.get('followers', 0):,}",
        'following': f"{stats.get('following', 0):,}",
        'contributions': f"{stats.get('contributions', 0):,}"
    }
