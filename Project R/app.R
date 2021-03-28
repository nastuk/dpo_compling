library(shiny)
library(timevis)

#read.csv("C:/Users/User/Desktop/Multimodal_Dict/study_verb.csv")
#mydata <- read.csv("C:/Users/User/Desktop/Multimodal_Dict/study_verb.csv", header = TRUE, encoding = "UTF-8")

study <- data.frame(
  id      = 1:4,
  content = c("To apply the mind to the acquisition of learning", "To follow  educational or professional studies at a university", "To be in doubt or perplexity", "To exercise oneself"),
  start   = c("1300-01-01", "1450-01-01", "1362-01-01","1450-01-01"),
  end     = c("2021-01-01", "2021-01-01", "1586-01-01","1474-01-01"),
  type    = "range"
)

learn <- data.frame(
  id      = 1:4,
  content = c("To acquire knowledge of a subject or skill ", "to find out", "To teach a person to do or how to do something", "To inform a person of something"),
  start   = c("900-01-01", "1629-01-01", "1340-01-01","1425-01-01"),
  end     = c("2021-01-01", "2021-01-01", "2021-01-01","1697-01-01"),
  type    = "range"
)

educate <- data.frame(
  id      = 1:4,
  content = c("To bring up children or animals by supply of food and attention to physical wants", "To provide schooling for young persons", "To train any person so as to develop the intellectual and moral powers generally", "To train animals"),
  start   = c("1607-01-01", "1588-01-01", "1849-01-01","1850-01-01"),
  end     = c("1818-01-01", "2021-01-01", "2021-01-01","2021-01-01"),
  type    = "point",
  style = c("color: red;", NA, NA)
)

ui <- fluidPage(
  titlePanel("The semantic changes of topic group 'Education'"),
  
  sidebarLayout(
      sidebarPanel(
        selectInput("Word",
                    "Choose a word:",
                    choices = c('study', 'educate', 'learn'),
                    selected = "educate")
      ),
    
      mainPanel(
         timevisOutput("timeline")
      )
   )
)

server <- function(input, output, session) {
  output$timeline <- renderTimevis({
    timevis(educate)
  })
}

shinyApp(ui = ui, server = server)

