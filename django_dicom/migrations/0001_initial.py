# Generated by Django 2.1.7 on 2019-03-25 10:50

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_dicom.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_uid', models.CharField(max_length=64, unique=True, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d+)*$', code='invalid_uid', message='Digits and dots only!')], verbose_name='Instance UID')),
                ('file', models.FileField(blank=True, upload_to='dicom')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Instance Number')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NIfTI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=64, unique=True)),
                ('given_name', models.CharField(blank=True, max_length=64, null=True)),
                ('family_name', models.CharField(blank=True, max_length=64, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=64, null=True)),
                ('name_prefix', models.CharField(blank=True, max_length=64, null=True)),
                ('name_suffix', models.CharField(blank=True, max_length=64, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=6, null=True)),
                ('is_updated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_uid', models.CharField(help_text='Unique identifier of the series', max_length=64, unique=True, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d+)*$', code='invalid_uid', message='Digits and dots only!')], verbose_name='Series UID')),
                ('date', models.DateField(blank=True, help_text='Date the series started', null=True, verbose_name='Series Date')),
                ('time', models.TimeField(blank=True, help_text='Time the series started', null=True, verbose_name='Series Time')),
                ('description', models.CharField(blank=True, help_text='Description of the series', max_length=64, null=True, verbose_name='Series Description')),
                ('number', models.IntegerField(blank=True, help_text='A number that identifies this series within a given session', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Series Number')),
                ('echo_time', models.FloatField(blank=True, help_text='Time in ms between the middle of the excitation pulse and the peak of the echo produced', null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('inversion_time', models.FloatField(blank=True, help_text='Time in milliseconds after the middle of inverting RF pulse to middle of excitation pulse to detect the amount of longitudinal magnetization', null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('repetition_time', models.FloatField(blank=True, help_text='The period of time in milliseconds between the beginning of a pulse sequence and the beginning of the succeeding pulse sequence.', null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('scanning_sequence', django_dicom.models.fields.ChoiceArrayField(base_field=models.CharField(choices=[('SE', 'Spin Echo'), ('IR', 'Inversion Recovery'), ('GR', 'Gradient Recalled'), ('EP', 'Echo Planar'), ('RM', 'Research Mode')], max_length=2), blank=True, help_text='Description of the type of data taken', null=True, size=5)),
                ('sequence_variant', django_dicom.models.fields.ChoiceArrayField(base_field=models.CharField(choices=[('SK', 'Segmented k-Space'), ('MTC', 'Magnetization Transfer Contrast'), ('SS', 'Steady State'), ('TRSS', 'Time Reversed Steady State'), ('SP', 'Spoiled'), ('MP', 'MAG Prepared'), ('OSP', 'Oversampling Phase'), ('NONE', 'None')], max_length=4), blank=True, help_text='Variant of the scanning sequence', null=True, size=None)),
                ('pixel_spacing', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]), blank=True, help_text='Physical distance in the patient between the center of each pixel, specified by a numeric pair: adjacent row spacing (delimiter) adjacent column spacing in mm', null=True, size=2)),
                ('manufacturer', models.CharField(blank=True, help_text='Manufacturer of the equipment that produced the composite instances', max_length=64, null=True)),
                ('manufacturer_model_name', models.CharField(blank=True, help_text="Manufacturer's model name of the equipment that produced the composite instances", max_length=64, null=True)),
                ('magnetic_field_strength', models.FloatField(blank=True, help_text='Nominal field strength of MR magnet, in Tesla', null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('device_serial_number', models.CharField(blank=True, help_text="Manufacturer's serial number of the equipment that produced the Composite Instances", max_length=64, null=True)),
                ('body_part_examined', models.CharField(blank=True, help_text='Text description of the part of the body examined', max_length=16, null=True)),
                ('patient_position', models.CharField(blank=True, choices=[('HFP', 'Head First-Prone'), ('HFS', 'Head First-Supine'), ('HFDR', 'Head First-Decubitus Right'), ('HFDL', 'Head First-Decubitus Left'), ('FFDR', 'Feet First-Decubitus Right'), ('FFDL', 'Feet First-Decubitus Left'), ('FFP', 'Feet First-Prone'), ('FFS', 'Feet First-Supine'), ('LFP', 'Left First-Prone'), ('LFS', 'Left First-Supine'), ('RFP', 'Right First-Prone'), ('RFS', 'Right First-Supine'), ('AFDR', 'Anterior First-Decubitus Right'), ('AFDL', 'Anterior First-Decubitus Left'), ('PFDR', 'Posterior First-Decubitus Right'), ('PFDL', 'Posterior First-Decubitus Left')], default='HFS', help_text='Patient position descriptor relative to the equipment', max_length=4, null=True)),
                ('modality', models.CharField(blank=True, choices=[('AR', 'Autorefraction'), ('ASMT', 'Content Assessment Results'), ('AU', 'Audio'), ('BDUS', 'Bone Densitometry (ultrasound)'), ('BMD', 'Bone Densitometry (X-Ray)'), ('BI', 'Biomagnetic imaging'), ('CR', 'Computed Radiography'), ('CT', 'Computed Tomography'), ('CTPROTOCOL', 'CT Protocol (Performed)'), ('DG', 'Diaphanography'), ('DOC', 'Document'), ('DX', 'Digital Radiography'), ('ECG', 'Electrocardiography'), ('EPS', 'Cardiac Electrophysiology'), ('EDS', 'Endoscopy'), ('FID', 'Fiducials'), ('GM', 'General Microscopy'), ('HC', 'Hard Copy'), ('HD', 'Hemodynamic Waveform'), ('IO', 'Intra-Oral Radiography'), ('IOL', 'Intraocular Lens Data'), ('IVOCT', 'Intravascular Optical Coherence Tomography'), ('IVUS', 'Intravascular Ultrasound'), ('KER', 'Keratometry'), ('KO', 'Key Object Selection'), ('LEN', 'Lensometry'), ('LS', 'Laser surface scan'), ('MG', 'Mammography'), ('MR', 'Magnetic Resonance'), ('M3D', 'Model for 3D Manufacturing'), ('NM', 'Nuclear Medicine'), ('OAM', 'Ophthalmic Axial Measurements'), ('OCT', 'Optical Coherence Tomography (non-Ophthalmic)'), ('OP', 'Ophthalmic Photography'), ('OPM', 'Ophthalmic Mapping'), ('OPT', 'Ophthalmic Tomography'), ('OPTBSV', 'Ophthalmic Tomography B-scan Volume Analysis'), ('OPTENF', 'Ophthalmic Tomography En Face'), ('OPV', 'Ophthalmic Visual Field'), ('OSS', 'Optical Surface Scan'), ('OT', 'Other'), ('PLAN', 'Plan'), ('PR', 'Presentation State'), ('PT', 'Positron emission tomography (PET)'), ('PX', 'Panoramic X-Ray'), ('REG', 'Registration'), ('RESP', 'Respiratory Waveform'), ('RF', 'Radio Fluoroscopy'), ('RG', 'Radiographic imaging (conventional film/screen)'), ('RTDOSE', 'Radiotherapy Dose'), ('RTIMAGE', 'Radiotherapy Image'), ('RTPLAN', 'Radiotherapy Plan'), ('RTRECORD', 'RT Treatment Record'), ('RTSTRUCT', 'Radiotherapy Structure Set'), ('RWV', 'Real World Value Map'), ('SEG', 'Segmentation'), ('SM', 'Slide Microscopy'), ('SMR', 'Stereometric Relationship'), ('SR', 'SR Document'), ('SRF', 'Subjective Refraction'), ('STAIN', 'Automated Slide Stainer'), ('TG', 'Thermography'), ('US', 'Ultrasound'), ('VA', 'Visual Acuity'), ('XA', 'X-Ray Angiography'), ('XC', 'External-camera Photography')], default='MR', help_text='Type of equipment that originally acquired the data used to create the images in this series', max_length=10, null=True)),
                ('institution_name', models.CharField(blank=True, help_text='Institution where the equipment that produced the Composite Instances is located', max_length=64, null=True)),
                ('protocol_name', models.CharField(blank=True, help_text='User-defined description of the conditions under which the series was performed', max_length=64, null=True)),
                ('flip_angle', models.FloatField(blank=True, help_text='Steady state angle in degrees to which the magnetic vector is flipped from the magnetic vector of the primary field.', null=True)),
                ('mr_acquisition_type', models.CharField(blank=True, choices=[('2D', '2D'), ('3D', '3D')], default='2D', help_text='Identification of data encoding scheme', max_length=2, null=True)),
                ('is_updated', models.BooleanField(default=False, help_text='Series fields were updated from instance headers')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_uid', models.CharField(max_length=64, unique=True, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d+)*$', code='invalid_uid', message='Digits and dots only!')], verbose_name='Study UID')),
                ('description', models.CharField(max_length=64)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('is_updated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Studies',
            },
        ),
        migrations.AddIndex(
            model_name='study',
            index=models.Index(fields=['study_uid'], name='django_dico_study_u_a6544a_idx'),
        ),
        migrations.AddField(
            model_name='series',
            name='_nifti',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_dicom.NIfTI'),
        ),
        migrations.AddField(
            model_name='series',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_dicom.Patient'),
        ),
        migrations.AddField(
            model_name='series',
            name='study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_dicom.Study'),
        ),
        migrations.AddField(
            model_name='patient',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mri_patient_set', to='research.Subject'),
        ),
        migrations.AddField(
            model_name='instance',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_dicom.Series'),
        ),
        migrations.AddIndex(
            model_name='series',
            index=models.Index(fields=['series_uid'], name='django_dico_series__1e48d6_idx'),
        ),
        migrations.AddIndex(
            model_name='series',
            index=models.Index(fields=['date', 'time'], name='django_dico_date_c6f151_idx'),
        ),
        migrations.AddIndex(
            model_name='patient',
            index=models.Index(fields=['patient_id'], name='django_dico_patient_2ebf71_idx'),
        ),
        migrations.AddIndex(
            model_name='patient',
            index=models.Index(fields=['date_of_birth'], name='django_dico_date_of_49f161_idx'),
        ),
        migrations.AddIndex(
            model_name='instance',
            index=models.Index(fields=['instance_uid'], name='django_dico_instanc_912612_idx'),
        ),
        migrations.AddIndex(
            model_name='instance',
            index=models.Index(fields=['date', 'time'], name='django_dico_date_e1bad8_idx'),
        ),
    ]
