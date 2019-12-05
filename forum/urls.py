from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('question', QuestionView)
router.register('question-tags', QuestionTagView)
router.register('answer', AnswerView)
router.register('question-up-vote', QUpVotesView)
router.register('answer-up-vote', AUpVotesView)
urlpatterns = router.urls
