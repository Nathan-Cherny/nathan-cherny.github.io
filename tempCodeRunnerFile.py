        headerFirstLine = """<header id="site-header" class="header-footer-group">"""
        header = (
            headerFirstLine
            + htmlContent.split("""<main id="site-content">""")[0].split(headerFirstLine)[1]
        )

        htmlContent = htmlContent.replace(header, newHeader)