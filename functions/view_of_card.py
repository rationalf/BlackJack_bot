def view_of_card(rank, suit):
    '''Function for making sticker from card'''
    if suit == "Clubs":
        if rank == 2:
            return "CAACAgUAAxkBAAEJmx5kpebc_XlwoOaxJR7AXpOnMN9LjgAC7gADzD_AVUNl620pf85VLwQ"
        elif rank == 3:
            return "CAACAgUAAxkBAAEJmyBkpecF9ZOmrnEkjJSTYpndbhjp-QACxAADjXXJVSgF1c4SfQRVLwQ"
        elif rank == 4:
            return "CAACAgUAAxkBAAEJmyJkpecnUi0fkXBD2IPd0ajk9ProjQAC1QADdn3BVdsjMJCRrwM-LwQ"
        elif rank == 5:
            return "CAACAgUAAxkBAAEJmyRkpedGJAOB-Eb7mW_2ewlAEER6_gACQQEAAqyuwFUKLvZfnYor0C8E"
        elif rank == 6:
            return "CAACAgUAAxkBAAEJmyZkpedrVZtaKIWayjNNgY8OZYDL1wACLAEAAvSuwVXTZanNGx7wAi8E"
        elif rank == 7:
            return "CAACAgUAAxkBAAEJmyhkpeeOYeM-MW2LV73sKC92gUX2HAAC6QADmpzAVfqejKTvA09xLwQ"
        elif rank == 8:
            return "CAACAgUAAxkBAAEJmypkpeepvj0QZndAlV_mdXS-oeY7rwACZQEAAmsnwFXzDbUvNrlSIC8E"
        elif rank == 9:
            return "CAACAgUAAxkBAAEJmyxkpefM61NNGnMneYUjIgUYSHemHQACHwEAAoPTwVX0XbSdYZTway8E"
        elif rank == 10:
            return "CAACAgUAAxkBAAEJmy5kpefwbrb2TsRWyNEIJjutMODUEgACWAEAApCMwFVqmiojuRUZnS8E"
        elif rank == 11:
            return "CAACAgUAAxkBAAEJmzNkpegaKtyqghX1MSA3PoDjokOT7QACSgEAArVSwVWnJirONvGsjC8E"
        elif rank == 12:
            return "CAACAgUAAxkBAAEJmzVkpeg_F5oR74pLOEGeXqWpbPkKsQACYwEAAtZUwVVB9Jrr699DBi8E"
        elif rank == 13:
            return "CAACAgUAAxkBAAEJmzlkpehd3B_CsFR_HIsOBN7yIa4j6gACagEAArV1wFUsUwIdrbHrzi8E"
        else:
            return "CAACAgUAAxkBAAEJmztkpeiFpPsecJVyzK2mYSo9KoweagACVgEAAk7KwFUdsPO8bDy3zS8E"
    elif suit == "Hearts":
        if rank == 2:
            return "CAACAgUAAxkBAAEJm0JkpejBZ7Ps5jtZ_llkr3xUkyMcxAACwAEAAri0wFUoQPrcy55z9S8E"
        elif rank == 3:
            return "CAACAgUAAxkBAAEJm0RkpejjohHf8SAdYPZRw3YSNsG2WQACkgEAAi3FwVUyj7OilKkEQi8E"
        elif rank == 4:
            return "CAACAgUAAxkBAAEJm0hkpelZdPWuygoUMEy383WahLC8IAACnQEAAtIewFXlnnP4enKOES8E"
        elif rank == 5:
            return "CAACAgUAAxkBAAEJm0pkpelsKmtgxIAPzslWNHpurml6rQAC9wADiiHBVSWGu92DeH5pLwQ"
        elif rank == 6:
            return "CAACAgUAAxkBAAEJm0xkpel-GfQx7eK0qTW0SuTYDfW38AACuQEAAi7fwVUndFyOv1LeuS8E"
        elif rank == 7:
            return "CAACAgUAAxkBAAEJm05kpemOevuEQF0HotvlyRSCdAgYvAACZAEAAtV9wVVc2N-IuRlx0C8E"
        elif rank == 8:
            return "CAACAgUAAxkBAAEJm1BkpemZd1mAY0eOeCsCBR4b044s-QACWAEAAk-6wVUC0fBkmnNZvC8E"
        elif rank == 9:
            return "CAACAgUAAxkBAAEJm1JkpemkAnR8l-8s3OmCHL_TvgObjQACpAEAAoDywVXcV-kFLl4Goy8E"
        elif rank == 10:
            return "CAACAgUAAxkBAAEJm1RkpemyyecueMlXEPw5TDtCODL_DwACEQEAAkFbwFVuiN9FfpNZWS8E"
        elif rank == 11:
            return "CAACAgUAAxkBAAEJm1hkpenCAa-7Ny7MgmEbEhfMGy56GQACTwEAAuZ6wVVeHVQy8OtDZC8E"
        elif rank == 12:
            return "CAACAgUAAxkBAAEJm1Zkpem-Tsfs-zpYiuh3UXCKY4YUfwACVwEAAhgewFWcKPy_MO0FAi8E"
        elif rank == 13:
            return "CAACAgUAAxkBAAEJm1pkpenfmKP1bc0YZsq0I4FtyIrIlgACGQEAAhRTwVWjUBF47pA6ES8E"
        else:
            return "CAACAgUAAxkBAAEJm1xkpenriYn8gyGYgWl-lMvI2F5S0QACigEAAvSIwFVK_o4a4DzQaC8E"
    elif suit == "Spades":
        if rank == 2:
            return "CAACAgUAAxkBAAEJm15kpeuu42bO_JqrYPLjadF08QABtgUAAnYBAALPscBVqkQzr6Yem3ovBA"
        elif rank == 3:
            return "CAACAgUAAxkBAAEJm2Bkpeu5g-VGsCgYDhLjjyd6Dux-HwACiAEAAlr1wFXDzixQPWB0ay8E"
        elif rank == 4:
            return "CAACAgUAAxkBAAEJm2JkpevDdPKZxKxqgVkNJzmRQIjybAAC9QADkD_AVTCXjNsUgWFcLwQ"
        elif rank == 5:
            return "CAACAgUAAxkBAAEJm2RkpevOvtxcm6mTkVpRySZZRTsFhwACtgEAAnl5wVUt6BMU1V4rQS8E"
        elif rank == 6:
            return "CAACAgUAAxkBAAEJm2ZkpevYV40CGjF0yRyAx-CJoU2rTgACwgEAAhMZyFUVAQk2w9IUoy8E"
        elif rank == 7:
            return "CAACAgUAAxkBAAEJm2hkpevkc9gbeZecNow13mgMZm_XRgACXwEAAlcqwVWYKA6AaDeLNC8E"
        elif rank == 8:
            return "CAACAgUAAxkBAAEJm2pkpevuZCRgs3IuRWmGNCt2QQfaSQAC5gEAApGAwFVYXzYRg5l2hS8E"
        elif rank == 9:
            return "CAACAgUAAxkBAAEJm2xkpev7r506r0Ux3uKSe44kS9FaSAACTAEAAlTbwVUOieck2aRPdC8E"
        elif rank == 10:
            return "CAACAgUAAxkBAAEJm25kpewGDon8FBUcRD96bqP62NQvywACfgEAAjEccVarx0aBCU7B3C8E"
        elif rank == 11:
            return "CAACAgUAAxkBAAEJm3BkpewQJOW4JIu_ZaqpV5nIdG1cMgACgQEAAg1zwFVqLPJXSoY2rC8E"
        elif rank == 12:
            return "CAACAgUAAxkBAAEJm3JkpewZ5-8sI6HkgA9yHYwvLXN01QACqQIAAomTwFVYoAJh92UFLi8E"
        elif rank == 13:
            return "CAACAgUAAxkBAAEJm3RkpewjwYqjj3CkcuAXu84UGuoDEAACpQEAAmtpwFXgo7SNLAsgqC8E"
        else:
            return "CAACAgUAAxkBAAEJm3ZkpewsuZ1xIbwvTOUFK9xxZKfFlwACewEAAoCZwFXg-Nr-7hZaoC8E"
    else:
        if rank == 2:
            return "CAACAgUAAxkBAAEJm3hkpew51Ld1sEqrbHrQYW2NH9wb9AACBgEAAmovyFWY6dj4c94fYi8E"
        elif rank == 3:
            return "CAACAgUAAxkBAAEJm3pkpexezDIYng-nOKmLxscC_Ha8cQAClQEAAuvlwVUAAfo2HFjA-HkvBA"
        elif rank == 4:
            return "CAACAgUAAxkBAAEJm3xkpexsg2H2fR8VUQZbVvEbdCLk2AACwQEAAqDNwFWiDdTqzKK29i8E"
        elif rank == 5:
            return "CAACAgUAAxkBAAEJm35kpex5YialkcnlbKEcY_WAPrLbTgACmQEAApEgwVUDWtfULkqa7i8E"
        elif rank == 6:
            return "CAACAgUAAxkBAAEJm4BkpeyFmiiiQk7cG63KIhJKbEfvdwACFwEAAvt_wVWgx6nKpXzQYi8E"
        elif rank == 7:
            return "CAACAgUAAxkBAAEJm4JkpeyOSUJSR8BTqwmkJgOf4WbX0AACjQEAArJWwFW0ccMe7TSgKi8E"
        elif rank == 8:
            return "CAACAgUAAxkBAAEJm4RkpeyZELqffzkbjp9eGLDD28QiVAACXQEAAmtEwFWjpcTqT8Nj4S8E"
        elif rank == 9:
            return "CAACAgUAAxkBAAEJm4ZkpeyjonqWXsIYxLrmpdnbZgOagwACNQEAAuQkwVVVg-Fo5xtXQi8E"
        elif rank == 10:
            return "CAACAgUAAxkBAAEJm4hkpeyugogPeik0CjELnKAcF7xpWgACUgEAAhlbwFV8m-J7WE21Ki8E"
        elif rank == 11:
            return "CAACAgUAAxkBAAEJm4pkpey57_Z1KYguCylkaT4h_NhGCgACTQEAAnHCyVW3tBaN5V6XEC8E"
        elif rank == 12:
            return "CAACAgUAAxkBAAEJm4xkpezHKv6OHQbB6E2l5B39Z-yC_gACuAEAArhlwFVXtlTiCEWnDS8E"
        elif rank == 13:
            return "CAACAgUAAxkBAAEJm45kpezRWxGpcgqY1BYRg5r6CihfkgACfgEAArn-wVWBh7R834WGzy8E"
        else:
            return "CAACAgUAAxkBAAEJm5BkpezbeDgmayw31whR3tGbXGNmdgACTAEAArlrwVUCjF9P-WDqbC8E"
