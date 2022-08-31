from logging import Filter

from django.db import models


class Voluntario(models.Model):
    no=''
    mi='ministerial'
    an='anciano'

    hb='hab'
    nhb='no'

    PRIV_CHOICES =[  
        (mi,'ministerial'),
        (an,'anciano'),
        (no,'ninguno'),
        ]

    HABILIT_CHOICES =[
        (hb,'si'),
        (nhb,'no'),
        (no,'ninguno'),
        ]

    voluntario_Id = models.AutoField(primary_key =True)
    nombres   =     models.CharField(max_length=20, null=False)
    apellidos  =    models.CharField(max_length=20, null=False)
    habilit_plataf =models.CharField(max_length=14,choices=HABILIT_CHOICES, default = no, blank=True)
    habilit_microf =models.CharField(max_length=14,choices=HABILIT_CHOICES, default = hb, blank=True)
    habilit_Zoom =  models.CharField(max_length=14,choices=HABILIT_CHOICES, default = no, blank=True)
    habilit_acomod =models.CharField(max_length=14,choices=HABILIT_CHOICES, default = hb, blank=True)
    habilit_presid =models.CharField(max_length=14,choices=HABILIT_CHOICES, default = no, blank=True)
    habilit_lector =models.CharField(max_length=14,choices=HABILIT_CHOICES, default = no, blank=True)
    privilegio =    models.CharField(max_length =12, choices= PRIV_CHOICES, default = no, blank=True)
    
    
    
    class Meta:
        ordering = ['nombres','apellidos']

    def __str__(self):
        txt ="{0} {1}"
        return txt.format(self.nombres, self.apellidos)

    def nombrecompleto(self):
        txt ="{0} {1}"
        return txt.format(self.nombres, self.apellidos)


class Plataforma (models.Model):
    
    plataf_Id= models.AutoField (primary_key =True)
    fecha = models.DateField( blank= True)
    voluntario_Id = models.ForeignKey (Voluntario, limit_choices_to= {'habilit_plataf':'hab'}, null=False, blank= False ,on_delete = models.CASCADE,)
    
    class Meta:
        ordering = ['fecha','voluntario_Id']

    def __str__(self):
        txt ="{0} {1}"
        return txt.format(self.fecha, self.voluntario_Id)





class Microfono (models.Model):
 
    microfono_Id= models.AutoField (primary_key =True)
    fecha = models.DateField( blank= True)
    voluntarioUno = models.ForeignKey (Voluntario, related_name='Microfonos' ,limit_choices_to= {'habilit_microf':'hab'}, null=True, blank= False ,on_delete = models.CASCADE,)
    voluntarioDos = models.ForeignKey (Voluntario, limit_choices_to= {'habilit_microf':'hab'}, null=False, blank= False ,on_delete = models.CASCADE,)
    
    class Meta:
        ordering = ['fecha']


    def __str__(self):
        txt ="{0} {1} {2}"
        return txt.format(self.fecha, self.voluntarioUno,self.voluntarioDos )  





class Zoom (models.Model):
 
    Zoom_Id= models.AutoField (primary_key =True)
    fecha = models.DateField( blank= True)
    voluntario_Id = models.ForeignKey (Voluntario, limit_choices_to= {'habilit_Zoom':'hab'}, null=False, blank= False ,on_delete = models.CASCADE,)
    
    class Meta:
        ordering = ['fecha','voluntario_Id']


    def __str__(self):
        txt ="{0} {1}"
        return txt.format(self.fecha, self.voluntario_Id) 
   



class Acomodador (models.Model):
  

    acomodador_Id= models.AutoField (primary_key =True)
    fecha = models.DateField( blank= True)
    voluntarioUno = models.ForeignKey (Voluntario, related_name='acomodadors' ,limit_choices_to= {'habilit_acomod':'hab'},null=True, blank= False ,on_delete = models.CASCADE,)
    voluntarioDos = models.ForeignKey (Voluntario,limit_choices_to= {'habilit_acomod':'hab'},null=False, blank= False ,on_delete = models.CASCADE,)
    
    class Meta:
        ordering = ['fecha']

    def __str__(self):
        txt ="{0} {1} {2}"
        return txt.format(self.fecha, self.voluntarioUno,self.voluntarioDos)

class Presidente (models.Model):
    
    presid_Id= models.AutoField (primary_key =True)
    fecha = models.DateField( blank= True)
    voluntario_Id = models.ForeignKey (Voluntario, limit_choices_to= {'habilit_presid':'hab'}, null=False, blank= False ,on_delete = models.CASCADE,)
    
    class Meta:
        ordering = ['fecha','voluntario_Id']

    def __str__(self):
        txt ="{0} {1}"
        return txt.format(self.fecha, self.voluntario_Id)

class Lector (models.Model):
    
    lector_Id= models.AutoField (primary_key =True)
    fecha = models.DateField( blank= True)
    voluntario_Id = models.ForeignKey (Voluntario, limit_choices_to= {'habilit_lector':'hab'}, null=False, blank= False ,on_delete = models.CASCADE,)
    
    class Meta:
        ordering = ['fecha','voluntario_Id']

    def __str__(self):
        txt ="{0} {1}"
        return txt.format(self.fecha, self.voluntario_Id)

