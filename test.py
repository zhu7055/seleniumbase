from seleniumbase import SB

with SB(test=True, uc=True) as sb:
    sb.open("https://google.com/ncr")
    sb.type('[title="Search"]', "tech with tim\n")
    sb.click('[href*="https://www.youtube.com/c/TechWithTim"]')
    sb.save_screenshot_to_logs()  # ./latest_logs/
    print(sb.get_page_title())
