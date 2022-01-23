class PostForm(FlaskForm):
    title = StringField('Blog Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')