        contentSplit = htmlContent.split("\n")
        l = [contentSplit.index(i) - 2 for i in contentSplit if f"<a href=\"/{path}/\"" in i]
        a = [i for i in l if "menu-item" in contentSplit[i]]
        if len(a) == 0: continue
        contentSplit[a[0]] = contentSplit[a[0]].replace("class=\"", "class=\"current-menu-item ")

        htmlContent = "\n".join(contentSplit)