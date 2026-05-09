import asyncio
import os
import sys

# Set dummy token for startup check
os.environ['TOKEN'] = 'mock_token'

# Add scratch to path for mock discord
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Add parent directory to path so we can import main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mock dotenv
class MockDotEnv:
    def load_dotenv(self): pass
sys.modules['dotenv'] = MockDotEnv()

from main import PurelinkBot

async def run_test():
    print("--- PURELINK MULTI-SERVICE TEST ---")
    bot = PurelinkBot()
    
    test_urls = [
        "https://www.instagram.com/reel/DXgTPwuDlbd?igsh=bmozaWVpNWhqdDFj",
        "https://youtu.be/WDoxNTBrvzQ?si=QL9lPjwL2q35h6dC",
        "https://open.spotify.com/track/4EDmwV0cTLJ31s9sLQ1x2p?si=kXsEHkrkSbmETyUy8Sd_7w",
        "https://www.amazon.com/gp/product/B0FK1GVJFV?tag=shopeva-20",
        "https://www.macys.com/shop/product/tour-edge-exotics-ls-right-hand-mens-x2013-9.0-ventus-blue-blk-stiff-driver?ID=25142710",
        "https://www.amazon.com/dp/B002KE7JB2?ref=t_ac_spc_accepted_tile&linkCode=tr1&tag=shopeva-20&linkId=B002KE7JB2_1777066761651"
    ]
    
    for url in test_urls:
        print(f"\nINPUT:  {url}")
        result = await bot.unwrap_link(url)
        print(f"OUTPUT: {result}")
        
if __name__ == "__main__":
    asyncio.run(run_test())
