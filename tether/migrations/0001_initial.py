# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-23 05:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobby_name', models.CharField(max_length=200)),
                ('game_mode', models.CharField(max_length=200)),
                ('match_id', models.CharField(max_length=200)),
                ('human_players', models.IntegerField()),
                ('engine', models.IntegerField()),
                ('game_mode_name', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('cluster', models.IntegerField()),
                ('start_time', models.IntegerField()),
                ('lobby_type', models.IntegerField()),
            ],
            options={
                'db_table': 'common_data',
            },
        ),
        migrations.CreateModel(
            name='DotaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tower_status_radiant', models.IntegerField()),
                ('radiant_win', models.BooleanField()),
                ('pre_game_duration', models.IntegerField()),
                ('tower_status_dire', models.IntegerField()),
                ('barracks_status_radiant', models.IntegerField()),
                ('flags', models.IntegerField()),
                ('leagueid', models.IntegerField()),
                ('match_id', models.CharField(max_length=200)),
                ('cluster_name', models.CharField(max_length=200)),
                ('positive_votes', models.IntegerField()),
                ('radiant_score', models.IntegerField()),
                ('match_seq_num', models.BigIntegerField()),
                ('barracks_status_dire', models.IntegerField()),
                ('first_blood_time', models.IntegerField()),
                ('dire_score', models.IntegerField()),
                ('negative_votes', models.IntegerField()),
            ],
            options={
                'db_table': 'dota_data',
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=255, unique=True)),
                ('region', models.CharField(max_length=255)),
                ('skill_level', models.CharField(blank=True, choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Diamond', 'Diamond')], default='BZ', max_length=255)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('password_status', models.CharField(blank=True, max_length=3, null=True)),
                ('players', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'league',
            },
        ),
        migrations.CreateModel(
            name='LeagueMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_skill', models.DecimalField(decimal_places=2, default='500', max_digits=6)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.League')),
            ],
            options={
                'db_table': 'league_membership',
            },
        ),
        migrations.CreateModel(
            name='MatchData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backpack_2', models.IntegerField()),
                ('item_4_name', models.CharField(max_length=200)),
                ('kills', models.IntegerField()),
                ('leaver_status_description', models.CharField(max_length=200)),
                ('item_0_name', models.CharField(max_length=200)),
                ('item_3_name', models.CharField(max_length=200)),
                ('hero_healing', models.IntegerField(blank=True, default=1, null=True)),
                ('gold_per_min', models.IntegerField()),
                ('hero_id', models.IntegerField()),
                ('item_0', models.IntegerField()),
                ('backpack_0', models.IntegerField()),
                ('scaled_hero_healing', models.IntegerField(blank=True, default=1, null=True)),
                ('scaled_tower_damage', models.IntegerField(blank=True, default=1, null=True)),
                ('assists', models.IntegerField()),
                ('item_4', models.IntegerField()),
                ('tower_damage', models.IntegerField()),
                ('item_1_name', models.CharField(max_length=200)),
                ('xp_per_min', models.IntegerField()),
                ('hero_damage', models.IntegerField()),
                ('item_2_name', models.CharField(max_length=200)),
                ('player_slot', models.IntegerField()),
                ('item_5_name', models.CharField(max_length=200)),
                ('gold', models.IntegerField()),
                ('level', models.IntegerField()),
                ('scaled_hero_damage', models.IntegerField()),
                ('denies', models.IntegerField()),
                ('item_5', models.IntegerField()),
                ('leaver_status', models.IntegerField()),
                ('item_3', models.IntegerField()),
                ('last_hits', models.IntegerField()),
                ('item_1', models.IntegerField()),
                ('item_2', models.IntegerField()),
                ('gold_spent', models.IntegerField()),
                ('hero_name', models.CharField(max_length=200)),
                ('backpack_1', models.IntegerField()),
                ('leaver_status_name', models.CharField(max_length=200)),
                ('deaths', models.IntegerField()),
            ],
            options={
                'db_table': 'match_data',
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('player1', models.CharField(default='', max_length=40)),
                ('player2', models.CharField(default='', max_length=40)),
                ('player3', models.CharField(default='', max_length=40)),
                ('player4', models.CharField(default='', max_length=40)),
                ('player5', models.CharField(default='', max_length=40)),
                ('player6', models.CharField(default='', max_length=40)),
                ('player7', models.CharField(default='', max_length=40)),
                ('player8', models.CharField(default='', max_length=40)),
                ('player9', models.CharField(default='', max_length=40)),
                ('player10', models.CharField(default='', max_length=40)),
                ('locked', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('winner', models.CharField(max_length=10, null=True)),
                ('lobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.League')),
            ],
            options={
                'db_table': 'matches',
            },
        ),
        migrations.CreateModel(
            name='MatchPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player0_id', models.BigIntegerField(null=True)),
                ('player3_id', models.BigIntegerField(null=True)),
                ('player1_id', models.BigIntegerField(null=True)),
                ('player4_id', models.BigIntegerField(null=True)),
                ('player2_id', models.BigIntegerField(null=True)),
                ('player7_id', models.BigIntegerField(null=True)),
                ('player8_id', models.BigIntegerField(null=True)),
                ('player9_id', models.BigIntegerField(null=True)),
                ('player6_id', models.BigIntegerField(null=True)),
                ('player5_id', models.BigIntegerField(null=True)),
            ],
            options={
                'db_table': 'match_players',
            },
        ),
        migrations.CreateModel(
            name='NewRecentMatches1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_match0', models.CharField(max_length=200)),
                ('id_match1', models.CharField(max_length=200)),
                ('id_match2', models.CharField(max_length=200)),
                ('id_match3', models.CharField(max_length=200)),
                ('id_match4', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Recent matches',
                'db_table': 'new_recent_matches1',
            },
        ),
        migrations.CreateModel(
            name='PlayersInMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.NewRecentMatches1')),
                ('players_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.MatchPlayers')),
            ],
            options={
                'verbose_name_plural': 'Recent matches',
                'db_table': 'players_in_match',
            },
        ),
        migrations.CreateModel(
            name='PrizePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_id', models.IntegerField()),
                ('prize_pool', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'prize_pool',
            },
        ),
        migrations.CreateModel(
            name='Profiles_Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.NewRecentMatches1')),
            ],
            options={
                'verbose_name_plural': 'Recent matches',
                'db_table': 'profiles_matches',
            },
        ),
        migrations.CreateModel(
            name='UserProfile1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('steam_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('win_rate', models.DecimalField(decimal_places=2, default='0000000000', max_digits=10)),
                ('average_gpm', models.DecimalField(decimal_places=2, default='000000', max_digits=6)),
                ('leagues', models.ManyToManyField(through='tether.LeagueMembership', to='tether.League')),
                ('recent_matches', models.ManyToManyField(through='tether.Profiles_Matches', to='tether.NewRecentMatches1')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile1',
            },
        ),
        migrations.AddField(
            model_name='profiles_matches',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.UserProfile1'),
        ),
        migrations.AddField(
            model_name='newrecentmatches1',
            name='players',
            field=models.ManyToManyField(through='tether.PlayersInMatch', to='tether.MatchPlayers'),
        ),
        migrations.AddField(
            model_name='leaguemembership',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.UserProfile1'),
        ),
        migrations.AlterUniqueTogether(
            name='leaguemembership',
            unique_together=set([('profile', 'league')]),
        ),
    ]