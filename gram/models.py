from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.

#class Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    picture = CloudinaryField('image')
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username

    @classmethod
    def update_profile(cls, id, user, bio, picture):
        cls.objects.filter(id=id).update(user=user, bio=bio, picture=picture)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()



#class Images
class Image(models.Model):
    image = CloudinaryField('images')
    image_name = models.CharField(max_length=30,blank=True)
    image_caption = models.CharField(max_length=300)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    comments = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.image_name

    @classmethod
    def update_image_caption(cls, id, image_caption):
        cls.objects.filter(id=id).update(image_caption=image_caption)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

# class Comment
class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(Image, on_delete=models.CASCADE)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def save_comment(self):
        self.user

    def delete_comment(self):
        self.delete()

 # class Follows
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    
class Like(models.Model):
  image =models.ForeignKey(Image, on_delete = models.CASCADE,related_name='photolikes')
  liker=models.ForeignKey(User,on_delete = models.CASCADE,related_name='userlikes')

  def __str__(self):
    return "%s like" % self.photo