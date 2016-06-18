from app import ic


@ic.route('/')
@ic.route('/index')
def index():
    return "I am Rahul Yadav"
