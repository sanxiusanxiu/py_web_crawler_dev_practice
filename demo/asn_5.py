import requests
import json
import time
from typing import Dict, Optional
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from urllib3 import Retry
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import random


class ASNLookup:
    def __init__(self):
        # 设置基础URL
        self.apis = {
            "ipwhois": "https://ipwhois.app/json/{ip}",
            "ripe": "https://stat.ripe.net/data/as-overview/data.json?resource={ip}",
            "bgpview": "https://api.bgpview.io/ip/{ip}",
            "ipinfo": "https://ipinfo.io/{ip}/json",
            "dbip": "https://api.db-ip.com/v2/YOUR_API_KEY/ip-info/{ip}"
        }

        # 配置代理
        self.proxies = {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890'
        }

        # 配置请求session
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """创建session"""
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        })
        # session.proxies.update(self.proxies)
        return session

    def query_ipwhois(self, ip: str) -> Optional[Dict]:
        """查询ipwhois.app"""
        try:
            response = self.session.get(
                self.apis["ipwhois"].format(ip=ip),
                timeout=10,
                verify=False
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "source": "ipwhois.app",
                    "asn": f"{data.get('asn', '')}",
                    "org": data.get("org", ""),
                    "isp": data.get("isp", ""),
                    "country": data.get("country", ""),
                    "region": data.get("region", ""),
                    "city": data.get("city", "")
                }
        except Exception as e:
            print(f"ipwhois查询出错: {e}")
        return None

    def query_bgpview(self, ip: str) -> Optional[Dict]:
        """查询BGPView API"""
        try:
            response = self.session.get(
                self.apis["bgpview"].format(ip=ip),
                timeout=10,
                verify=False
            )
            if response.status_code == 200:
                data = response.json().get("data", {})
                prefixes = data.get("prefixes", [{}])[0] if data.get("prefixes") else {}
                asn = prefixes.get("asn", {})
                return {
                    "source": "bgpview.io",
                    "asn": f"AS{asn.get('asn', '')}",
                    "org": asn.get("name", ""),
                    "description": asn.get("description", ""),
                    "country": asn.get("country_code", ""),
                    "prefix": prefixes.get("prefix", "")
                }
        except Exception as e:
            print(f"BGPView查询出错: {e}")
        return None

    def query_ripe(self, ip: str) -> Optional[Dict]:
        """查询RIPE"""
        try:
            response = self.session.get(
                self.apis["ripe"].format(ip=ip),
                timeout=10,
                verify=False
            )
            if response.status_code == 200:
                data = response.json()
                asn_info = data.get("data", {}).get("asns", [{}])[0]
                return {
                    "source": "ripe.net",
                    "asn": f"{asn_info.get('asn', '')}" if "AS" in str(asn_info.get('asn', '')).upper() else f"AS{asn_info.get('asn', '')}",
                    "org": asn_info.get("holder", ""),
                    "announced": asn_info.get("announced", False)
                }
        except Exception as e:
            print(f"RIPE查询出错: {e}")
        return None

    def query_ipinfo(self, ip: str) -> Optional[Dict]:
        """查询IPinfo"""
        try:
            response = self.session.get(
                self.apis["ipinfo"].format(ip=ip),
                timeout=10,
                verify=False
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "ip":ip,
                    "source": "ipinfo.io",
                    "asn": data.get("org", "").split()[0],  # ASN是org字段中的第一部分
                    "org": data.get("org", ""),
                    "city": data.get("city", ""),
                    "country": data.get("country", ""),
                    "region": data.get("region", "")
                }
        except Exception as e:
            print(f"IPinfo查询出错: {e}")
        return None

    def query_dbip(self, ip: str) -> Optional[Dict]:
        """查询DB-IP"""
        try:
            response = self.session.get(
                self.apis["dbip"].format(ip=ip),
                timeout=10,
                verify=False
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "source": "db-ip.com",
                    "asn": data.get("asn", ""),
                    "org": data.get("organization", ""),
                    "country": data.get("country", ""),
                    "city": data.get("city", "")
                }
        except Exception as e:
            print(f"DB-IP查询出错: {e}")
        return None

    def query_ip(self, ip: str) -> Dict:
        """查询单个IP的完整信息"""
        # 分别查询五个数据源
        # ipwhois_result = self.query_ipwhois(ip)
        # bgpview_result = self.query_bgpview(ip)
        # ripe_result = self.query_ripe(ip)
        ipinfo_result = self.query_ipinfo(ip)
        # dbip_result = self.query_dbip(ip)

        return {
            "ip": ip,
            # "ipwhois": ipwhois_result,
            # "bgpview": bgpview_result,
            # "ripe": ripe_result,
            "ipinfo": ipinfo_result
            # "dbip": dbip_result
        }


# 示例：执行查询
def read_ips(filename: str) -> list:
    """从文件读取IP列表"""
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"读取文件出错: {e}")
        return []

def save_results(results: list, filename: str):
    """保存结果，每行一个JSON"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for result in results:
                f.write(json.dumps(result, ensure_ascii=False) + '\n')
        print(f"\n结果已保存到 {filename}")
    except Exception as e:
        print(f"\n保存结果时出错: {e}")


def main():
    asn_lookup = ASNLookup()
    ip_file = "ip_1000.txt"
    ip_list = read_ips(ip_file)

    if not ip_list:
        print("IP列表为空")
        return

    all_results = []
    for ip in tqdm(ip_list, desc="正在查询"):
        print(f"\n正在查询IP: {ip}")
        result = asn_lookup.query_ip(ip)
        all_results.append(result)
        # number = make_random()
        time.sleep(1)

    # 保存每个数据源的结果到不同的文件
    # ipwhois_results = [result["ipwhois"] for result in all_results if result["ipwhois"]]
    # save_results(ipwhois_results, 'ipwhois_results.jsonl')
    #
    # bgpview_results = [result["bgpview"] for result in all_results if result["bgpview"]]
    # save_results(bgpview_results, 'bgpview_results.jsonl')
    #
    # ripe_results = [result["ripe"] for result in all_results if result["ripe"]]
    # save_results(ripe_results, 'ripe_results.jsonl')
    #
    ipinfo_results = [result["ipinfo"] for result in all_results if result["ipinfo"]]
    save_results(ipinfo_results, 'ipinfo_results.jsonl')
    #
    # dbip_results = [result["dbip"] for result in all_results if result["dbip"]]
    # save_results(dbip_results, 'dbip_results.jsonl')


if __name__ == "__main__":
    main()
