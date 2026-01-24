"""
GitHub統計データ取得モジュール

GitHub APIを使用してユーザーの統計情報を取得する。
外部サービス（github-readme-stats等）に依存せず、
直接APIから取得してテキスト表示する。
"""
import os
import re
from datetime import datetime, timedelta
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

    GitHub GraphQL APIを使用して過去1年間のコントリビューション数を取得。
    GITHUB_TOKEN環境変数が必要。

    Args:
        username: GitHubユーザー名

    Returns:
        年間コントリビューション数
    """
    token = os.environ.get('GITHUB_TOKEN')

    if not token:
        # トークンがない場合はスクレイピングにフォールバック
        return _fetch_contributions_scrape(username)

    # 過去1年間の日付を計算
    now = datetime.utcnow()
    one_year_ago = now - timedelta(days=365)

    query = """
    query($username: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $username) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """

    variables = {
        'username': username,
        'from': one_year_ago.isoformat() + 'Z',
        'to': now.isoformat() + 'Z'
    }

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(
            'https://api.github.com/graphql',
            json={'query': query, 'variables': variables},
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return 0

        data = response.json()
        contributions = (
            data.get('data', {})
            .get('user', {})
            .get('contributionsCollection', {})
            .get('contributionCalendar', {})
            .get('totalContributions', 0)
        )
        return contributions
    except (requests.RequestException, KeyError, TypeError):
        return 0


def _fetch_contributions_scrape(username: str) -> int:
    """
    スクレイピングでコントリビューション数を取得（フォールバック用）
    """
    url = f'https://github.com/{username}'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        }
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return 0

        match = re.search(
            r'([\d,]+)\s+contributions?\s+in\s+the\s+last\s+year',
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
