"""
GitHub統計データ取得のテスト

TDD: テストを先に書いてから実装する
"""
import pytest
from unittest.mock import patch, MagicMock


class TestGitHubStats:
    """GitHub統計データ取得のテストクラス"""

    def test_fetch_user_stats_returns_dict(self):
        """fetch_user_stats関数が辞書を返すことを確認"""
        from github_stats import fetch_user_stats

        with patch('github_stats.requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'public_repos': 42,
                'followers': 100,
                'following': 50,
                'public_gists': 5
            }
            mock_get.return_value = mock_response

            result = fetch_user_stats('yuki-mtmr')

            assert isinstance(result, dict)
            assert 'public_repos' in result
            assert 'followers' in result

    def test_fetch_user_stats_returns_correct_data(self):
        """fetch_user_stats関数が正しいデータを返すことを確認"""
        from github_stats import fetch_user_stats

        with patch('github_stats.requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'public_repos': 42,
                'followers': 100,
                'following': 50,
                'public_gists': 5
            }
            mock_get.return_value = mock_response

            result = fetch_user_stats('yuki-mtmr')

            assert result['public_repos'] == 42
            assert result['followers'] == 100
            assert result['following'] == 50

    def test_fetch_user_stats_handles_api_error(self):
        """API エラー時にデフォルト値を返すことを確認"""
        from github_stats import fetch_user_stats

        with patch('github_stats.requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            result = fetch_user_stats('nonexistent-user')

            assert result['public_repos'] == 0
            assert result['followers'] == 0

    def test_fetch_contributions_returns_count(self):
        """fetch_contributions関数が年間コントリビューション数を返すことを確認"""
        from github_stats import fetch_contributions

        with patch('github_stats.requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.text = '''
            <td class="ContributionCalendar-day" data-level="2" data-date="2024-01-01">1</td>
            <td class="ContributionCalendar-day" data-level="3" data-date="2024-01-02">2</td>
            '''
            mock_get.return_value = mock_response

            result = fetch_contributions('yuki-mtmr')

            assert isinstance(result, int)
            assert result >= 0

    def test_format_stats_for_display(self):
        """統計データを表示用にフォーマットする関数のテスト"""
        from github_stats import format_stats_for_display

        stats = {
            'public_repos': 42,
            'followers': 1234,
            'following': 50,
            'contributions': 567
        }

        result = format_stats_for_display(stats)

        assert '42' in result['repos']
        assert '1,234' in result['followers'] or '1234' in result['followers']
        assert '567' in result['contributions']

    def test_fetch_user_stats_handles_network_error(self):
        """ネットワークエラー時にデフォルト値を返すことを確認"""
        from github_stats import fetch_user_stats

        with patch('github_stats.requests.get') as mock_get:
            import requests
            mock_get.side_effect = requests.RequestException('Network error')

            result = fetch_user_stats('yuki-mtmr')

            assert result['public_repos'] == 0
            assert result['followers'] == 0

    def test_fetch_contributions_handles_network_error(self):
        """ネットワークエラー時に0を返すことを確認"""
        from github_stats import fetch_contributions

        with patch('github_stats.requests.get') as mock_get:
            import requests
            mock_get.side_effect = requests.RequestException('Network error')

            result = fetch_contributions('yuki-mtmr')

            assert result == 0

    def test_fetch_contributions_handles_404(self):
        """404エラー時に0を返すことを確認"""
        from github_stats import fetch_contributions

        with patch('github_stats.requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            result = fetch_contributions('nonexistent-user')

            assert result == 0

    def test_fetch_contributions_with_graphql(self):
        """GraphQL APIでコントリビューション数を取得できることを確認"""
        from github_stats import fetch_contributions
        import os

        with patch.dict(os.environ, {'GITHUB_TOKEN': 'test_token'}):
            with patch('github_stats.requests.post') as mock_post:
                mock_response = MagicMock()
                mock_response.status_code = 200
                mock_response.json.return_value = {
                    'data': {
                        'user': {
                            'contributionsCollection': {
                                'contributionCalendar': {
                                    'totalContributions': 456
                                }
                            }
                        }
                    }
                }
                mock_post.return_value = mock_response

                result = fetch_contributions('yuki-mtmr')

                assert result == 456

    def test_fetch_contributions_fallback_to_scrape(self):
        """トークンがない場合はスクレイピングにフォールバックすることを確認"""
        from github_stats import fetch_contributions
        import os

        with patch.dict(os.environ, {}, clear=True):
            # GITHUB_TOKENを削除
            if 'GITHUB_TOKEN' in os.environ:
                del os.environ['GITHUB_TOKEN']

            with patch('github_stats._fetch_contributions_scrape') as mock_scrape:
                mock_scrape.return_value = 123

                result = fetch_contributions('yuki-mtmr')

                mock_scrape.assert_called_once_with('yuki-mtmr')
                assert result == 123

    def test_default_stats_returns_zeros(self):
        """_default_stats関数がゼロ値を返すことを確認"""
        from github_stats import _default_stats

        result = _default_stats()

        assert result['public_repos'] == 0
        assert result['followers'] == 0
        assert result['following'] == 0
        assert result['public_gists'] == 0
