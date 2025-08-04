from seleniumbase import SB

with SB(test=True, uc=True) as sb:
    #Open your browser and visit the website
    sb.open("https://google.com/ncr")
    #Search
    sb.type('[title="Search"]', "tech with tim\n")
    #Click to go to the website
    sb.click('[href*="https://www.youtube.com/c/TechWithTim"]')
    #save the screenshot
    sb.save_screenshot_to_logs()  # ./latest_logs/
    print(sb.get_page_title())
