s = read.csv("superstore_dataset2011-2015.csv")


holiday = s[s$Order.Date <= "2011-12-31" && s$Order.Date >= "2011-11-20", ]


hol2011 = s[7334:8998,]
post2011 = s[8999:9691,]
hol2012 = s[18148:19961,]
post2012 = s[19961:20875,]
hol2013 = s[31589:33759,]
post2013 = s[33760:34896,]
xhol = s[48321:51290,]

hol = rbind(hol2011,hol2012,hol2013)
post = rbind(post2011,post2012,post2013)

data2011 = read.csv("newHol2011.csv")
data2012 = read.csv("newHol2012.csv")
data2013 = read.csv("newHol2013.csv")


Accessories = rbind(data2011[1,],data2012[1,],data2013[1,])
Appliances = rbind(data2011[2,],data2012[2,],data2013[2,])
Art = rbind(data2011[3,],data2012[3,],data2013[3,])
Binders = rbind(data2011[4,],data2012[4,],data2013[4,])
Bookcases = rbind(data2011[5,],data2012[5,],data2013[5,])
Chairs = rbind(data2011[6,],data2012[6,],data2013[6,])
Copiers = rbind(data2011[7,],data2012[7,],data2013[7,])
Envelopes = rbind(data2011[8,],data2012[8,],data2013[8,])
Fasteners = rbind(data2011[9,],data2012[9,],data2013[9,])
Furnishings = rbind(data2011[10,],data2012[10,],data2013[10,])
Labels = rbind(data2011[11,],data2012[11,],data2013[11,])
Machines = rbind(data2011[12,],data2012[12,],data2013[12,])
Paper = rbind(data2011[13,],data2012[13,],data2013[13,])
Phones = rbind(data2011[14,],data2012[14,],data2013[14,])
Storage = rbind(data2011[15,],data2012[15,],data2013[15,])
Supplies = rbind(data2011[16,],data2012[16,],data2013[16,])
Tables = rbind(data2011[17,],data2012[17,],data2013[17,])

PostRevenue = data.frame()

Accessorieslm =lm(Post.Revenue ~ Revenue - 1, data = Accessories)
PostRevenue = rbind(PostRevenue, predict(Accessorieslm,newdata=data.frame(xhol[1,2:3])))

Applianceslm =lm(Post.Revenue ~ Revenue - 1, data = Appliances)
PostRevenue = rbind(PostRevenue, predict(Applianceslm,newdata=xhol[2,2:3]))

Artlm =lm(Post.Revenue ~ Revenue - 1, data = Art)
PostRevenue = rbind(PostRevenue, predict(Artlm,newdata=xhol[3,2:3]))

Binderslm =lm(Post.Revenue ~ Revenue - 1, data = Binders)
PostRevenue = rbind(PostRevenue, predict(Binderslm,newdata=xhol[4,2:3]))

Bookcaseslm =lm(Post.Revenue ~ Revenue - 1, data = Bookcases)
PostRevenue = rbind(PostRevenue, predict(Bookcaseslm,newdata=xhol[5,2:3]))

Chairslm =lm(Post.Revenue ~ Revenue - 1, data = Chairs)
PostRevenue = rbind(PostRevenue, predict(Chairslm,newdata=xhol[6,2:3]))

Copierslm =lm(Post.Revenue ~ Revenue - 1, data = Copiers)
PostRevenue = rbind(PostRevenue, predict(Copierslm,newdata=xhol[7,2:3]))

Envelopeslm =lm(Post.Revenue ~ Revenue - 1, data = Envelopes)
PostRevenue = rbind(PostRevenue, predict(Envelopeslm,newdata=xhol[8,2:3]))

Fastenerslm =lm(Post.Revenue ~ Revenue - 1, data = Fasteners)
PostRevenue = rbind(PostRevenue, predict(Fastenerslm,newdata=xhol[9,2:3]))

Furnishingslm =lm(Post.Revenue ~ Revenue - 1, data = Furnishings)
PostRevenue = rbind(PostRevenue, predict(Furnishingslm,newdata=xhol[10,2:3]))

Labelslm =lm(Post.Revenue ~ Revenue - 1, data = Labels)
PostRevenue = rbind(PostRevenue, predict(Labelslm,newdata=xhol[11,2:3]))

Machineslm =lm(Post.Revenue ~ Revenue - 1, data = Machines)
PostRevenue = rbind(PostRevenue, predict(Machineslm,newdata=xhol[12:3,2:3]))

Paperlm =lm(Post.Revenue ~ Revenue - 1, data = Paper)
PostRevenue = rbind(PostRevenue, predict(Paperlm,newdata=xhol[13,2:3]))

Phoneslm =lm(Post.Revenue ~ Revenue - 1, data = Phones)
PostRevenue = rbind(PostRevenue, predict(Phoneslm,newdata=xhol[14,2:3]))

Storagelm =lm(Post.Revenue ~ Revenue - 1, data = Storage)
PostRevenue = rbind(PostRevenue, predict(Storagelm,newdata=xhol[15,2:3]))

Supplieslm =lm(Post.Revenue ~ Revenue - 1, data = Supplies)
PostRevenue = rbind(PostRevenue, predict(Supplieslm,newdata=xhol[16,2:3]))

Tableslm =lm(Post.Revenue ~ Revenue - 1, data = Tables)
PostRevenue = rbind(PostRevenue, predict(Tableslm,newdata=xhol[17,2:3]))
summary(Chairslm)

View(PostRevenue)


