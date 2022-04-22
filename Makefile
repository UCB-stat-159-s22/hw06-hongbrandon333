.PHONY : clean
clean :
    rm -f figures/*.png
    rm -f tables/*.csv

.PHONY : all
all :
    jupyter execute hw4_full.ipynb