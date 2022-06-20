import pandas as pd
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import warnings
import psycopg2
warnings.filterwarnings('ignore')

external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)
app.title = 'NFL Game Graph'

conn = psycopg2.connect()
cur = conn.cursor()

def create_pandas_table(sql_query, database = conn):
    table = pd.read_sql_query(sql_query, database)
    return table

df = create_pandas_table("SELECT * FROM play_by_play_data")

cur.close()
conn.close()

year_options = [2020, 2021]

week_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

info_markdown = '''
Data Source: https://www.nflfastr.com/

Created by: Tim Merkel
'''

nfl_logo_markdown ='''
![away logo](/assets/resized_image.png)
'''
header_markdown = '''
**NFL GAME GRAPH**
'''

app.layout = html.Div(children=[
    html.Div(
        dcc.Markdown(header_markdown),
            style={'grid-area': '1 / 2 / 2 / 6',
                   'backgroundColor':'#222222',
                   'color': 'white',
                   'font-family': 'Courier New, monospace',
                   'font-size': '2.5em'}
        ),
    html.Div(
        dcc.Markdown(nfl_logo_markdown),
        style={'grid-area': '1 / 1 / 2 / 2',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'text-align': 'center'
               }
        ),
    html.Div(
        dcc.Markdown(info_markdown),
        style={'grid-area': '1 / 6 / 2 / 9',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'text-align': 'right'
               }
        ),
    html.Div(
        dcc.Markdown(id='game-info-text1'),
        style={'grid-area': '2 / 3 / 3 / 4',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text2'),
        style={'grid-area': '2 / 4 / 3 / 5',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text3'),
        style={'grid-area': '2 / 5 / 3 / 6',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text4'),
        style={'grid-area': '2 / 6 / 3 / 7',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text5'),
        style={'grid-area': '2 / 7 / 3 / 8',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px',
               'text-align': 'center',
               'align-items': 'center'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text6'),
        style={'grid-area': '2 / 8 / 3 / 9',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px',
               'text-align': 'center'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text7'),
        style={'grid-area': '6 / 1 / 7 / 2',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px',
               'text-align': 'center',
               'align-items': 'center'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text8'),
        style={'grid-area': '6 / 2 / 7 / 3',
               'backgroundColor':'#222222',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px',
               'text-align': 'center',
               'align-items': 'center'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text9'),
        style={'grid-area': '7 / 1 / 9 / 2',
               'backgroundColor':'#333333',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px',
               'font-size': '0.9em'}
        ),
    html.Div(
        dcc.Markdown(id='game-info-text10'),
        style={'grid-area': '7 / 2 / 9 / 3',
               'backgroundColor':'#333333',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px',
               'font-size': '0.9em'}
        ),

    html.Div(['Select Year',
        dcc.Dropdown(
            id='year-picker',
            options=year_options,
            value=2021,
            style={#'grid-area': '2 / 1 / 3 / 2',
                   'backgroundColor':'white',
                   'color': '#333333'})],
        style={'grid-area': '2 / 1 / 3 / 3',
               'backgroundColor':'#333333',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px'}
        ),

    html.Div(['Select Week',
        dcc.Dropdown(
            id='week-picker',
            options=week_options,
            value=1,
            style={#'grid-area': '3 / 1 / 4 / 2',
                   'backgroundColor':'white',
                   'color': '#333333'})],
        style={'grid-area': '3 / 1 / 4 / 3',
               'backgroundColor':'#333333',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px'}
        ),

    html.Div(['Select Game',
        dcc.RadioItems(
            id='game-picker2',
            #options=['2021_01_ARI_TEN'],
            value='2021_01_ARI_TEN',
            style={#'grid-area': '4 / 1 / 5 / 2',
                   'backgroundColor':'#333333',
                   'color': 'white'})],
        style={'grid-area': '4 / 1 / 6 / 3',
               'backgroundColor':'#333333',
               'color': 'white',
               'font-family': 'Courier New, monospace',
               'border-top-style': 'solid',
               'border-color': 'lightgray',
               'border-width': '2px',
               'border-radius': '5px'},
        ),

    dcc.Graph(
        id='playbyplay-graph',
        #figure=fig,
        style={'grid-area': '3 / 3 / 9 / 7',
               'backgroundColor':'#222222'}
        ),

    dcc.Graph(
        id='wp-graph',
        #figure=fig2,
        style={'grid-area': '3 / 7 / 9 / 9',
               'backgroundColor':'#222222'}
        )

    ], style={
              'display': 'grid',
              'grid-template-columns': 'repeat(2, .125fr) repeat(3, .25fr) 1.25fr repeat(2, .125fr)',
              'grid-template-rows': 'repeat(4, .1fr) .55fr .1fr 1fr 1fr',
              'grid-column-gap': '5px',
              'grid-row-gap': '5px',
              'backgroundColor':'#222222',
              #'text-align':'center'
              })


#Filters week options by year
@app.callback(Output('week-picker', 'options'),
              [Input('year-picker', 'value')])
def get_week_options(selected_year):
    year_df = df[df['year']==selected_year]
    week_options = sorted(list(year_df['week'].unique()))
    return week_options


#Filters game options by week
@app.callback(Output('game-picker2', 'options'),
              [Input('week-picker', 'value')],
              [State('year-picker', 'value')])
def get_game_options(selected_week, selected_year):
    year_filtered_df = df[df['year']==selected_year]
    game_filtered_df = year_filtered_df[year_filtered_df['week']==selected_week]
    game_options2 = []
    for game in game_filtered_df['game_id'].unique():
        game_label = f' {str(game).split("_")[2]}@{str(game).split("_")[3]}'
        game_options2.append({'label':game_label, 'value':game})
    return game_options2


def create_playbyplay(game_id):
    selected_game_df = df.loc[df['game_id'] == game_id]
    selected_game_df.reset_index(inplace=True)
    selected_game_df['play_number'] = selected_game_df['index'].rank(method='dense')
    selected_game_df['next_play_number'] = selected_game_df['play_number'] + 1
    #selected_game_df.dropna(subset=['posteam'], inplace=True)
    current_quarter = 0
    wp_list = []
    play_list = []

    # COLOR MAP

    team_color_dict = {'ARI': '#97233F',
                       'ATL': '#A71930',
                        'BAL': '#241773',
                        'BUF': '#00338D',
                        'CAR': '#0085CA',
                        'CHI': '#0B162A',
                        'CIN': '#FB4F14',
                        'CLE': '#311D00',
                        'DAL': '#003594',
                        'DEN': '#FB4F14',
                        'DET': '#0076B6',
                        'GB': '#203731',
                        'HOU': '#03202F',
                        'IND': '#002C5F',
                        'JAX': '#101820',
                        'KC': '#E31837',
                        'LA': '#003594',
                        'LAC': '#0080C6',
                        'LV': '#000000',
                        'MIA': '#008E97',
                        'MIN': '#4F2683',
                        'NE': '#002244',
                        'NO': '#D3BC8D',
                        'NYG': '#0B2265',
                        'NYJ': '#125740',
                        'PHI': '#004C54',
                        'PIT': '#FFB612',
                        'SEA': '#002244',
                        'SF': '#AA0000',
                        'TB': '#D50A0A',
                        'TEN': '#0C2340',
                        'WAS': '#5A1414',
                         'GAME': 'black'}

    # PLAY BY PLAY GRAPH
    layout = go.Layout(#width=900,
                       height=1800,
                       showlegend=False,
                       paper_bgcolor='white',
                       plot_bgcolor='lightgray')

    layout.update(
                  xaxis=dict(range=[-10, 110], autorange=False, fixedrange=True),
                  yaxis=dict(range=[0.5, (selected_game_df['next_play_number'].max() - 0.5)], autorange=False, fixedrange=True))

    fig = go.Figure(layout=layout)

    for i, row in selected_game_df.iterrows():
        yardage_change = row['yardage_change']
        yard_line = row['actyrdln']
        no_play_flag = row['yards_gained']
        yards_gained = row['yards_gained']
        play_desc = row['play_desc']
        yardage_marker = dict(line=dict(color='black'))
        play_type = row['play_type']
        posteam = row['actposteam']
        away_team = row['away_team']
        home_team = row['home_team']
        desc = row['desc']
        anno = ''
        play_number = row['play_number']
        next_play_number = row['next_play_number']
        return_yards = row['return_yards']

        turnover_dict = {row['home_team']: row['away_team'],
                         row['away_team']: row['home_team']}

        wp_list.append(row['home_wp'])
        play_list.append(play_number)

        if row['posteam'] == row['away_team']:
            pos_color = team_color_dict[posteam]
            yardage_marker = dict(line=dict(color=pos_color))
            turnover_color = team_color_dict[home_team]
        else:
            pos_color = team_color_dict[posteam]
            yardage_marker = dict(line=dict(color=pos_color))
            turnover_color = team_color_dict[away_team]

        if i == 0:
            fig.add_trace(go.Bar(x=[-5], y=[(selected_game_df['next_play_number'].max() - 0.5)],
                             orientation='v', marker_color=team_color_dict[row['home_team']], width= 10,
                             marker=dict(line=dict(color='gray', width=0.5))
                             #pattern=dict(shape='|', fgcolor='black', fgopacity=0.5))
                             ))

            fig.add_trace(go.Bar(x=[105], y=[(selected_game_df['next_play_number'].max() - 0.5)],
                             orientation='v', marker_color=team_color_dict[row['away_team']], width= 10,
                             marker=dict(line=dict(color='gray', width=0.5))
                             #pattern=dict(shape='|', fgcolor='black', fgopacity=0.5))
                             ))

        if row['timeout'] == 1 or row['two_minute'] == True:
            no_play_flag = 0
            if yard_line == 0:
                yard_line = row['nextplay_actyrdln']
            timeout_marker = dict(symbol=25,
                                 line=dict(color=pos_color, width=0.5))

        elif 'incomplete' in play_desc:
            timeout_marker = dict(symbol=4,
                                 line=dict(color=pos_color, width=0.5))

        elif 'spike' in play_desc:
            no_play_flag = 0
            timeout_marker = dict(symbol=6,
                                 line=dict(color=pos_color, width=0.5))

        elif 'kneel' in play_desc:
            no_play_flag = 0
            timeout_marker = dict(symbol=10,
                                 line=dict(color=pos_color, width=0.5))

        elif row['interception'] == 1:
            no_play_flag = 1
            yardage_marker = dict(line=dict(
                                       color=pos_color,
                                       width=0.5),
                                  pattern=dict(
                                          shape='/',
                                          fgcolor=pos_color,
                                          fgopacity=1)
                                  )
            pos_color = turnover_color
            anno = 'INTERCEPTED'
            posteam = turnover_dict[posteam]

        elif row['fumble_lost'] == 1:
            no_play_flag = 1
            yardage_marker = dict(line=dict(
                                       color=pos_color,
                                       width=0.5),
                                  pattern=dict(
                                          shape='/',
                                          fgcolor=pos_color,
                                          fgopacity=1)
                                  )
            pos_color = turnover_color
            anno = 'FUMBLE'
            posteam = turnover_dict[posteam]

        elif row['punt_blocked'] == 1:
            no_play_flag = 1
            yardage_marker = dict(line=dict(
                                       color=pos_color,
                                       width=0.5),
                                  pattern=dict(
                                          shape='/',
                                          fgcolor=pos_color,
                                          fgopacity=1)
                                  )
            pos_color = turnover_color
            anno = 'BLOCKED'
            posteam = turnover_dict[posteam]

        elif play_type == 'field_goal' or play_type == 'extra_point' or 'ATTEMPT' in desc:
            if play_type == 'field_goal':
                if 'GOOD' in desc:
                    anno = 'FIELD GOAL GOOD'
                else:
                    anno = 'FIELD GOAL MISSED'
            elif play_type == 'extra_point':
                if 'GOOD' in desc:
                    anno = 'EXTRA POINT GOOD'
                else:
                    anno = 'EXTRA POINT MISSED'
            else:
                no_play_flag = 0
                if 'SUCCEEDS' in desc:
                    anno = '2-PT CONVERSION GOOD'
                else:
                    anno = '2-PT CONVERSION FAILED'
            if posteam == away_team:
                timeout_marker = dict(symbol=7, #size=100,
                                 line=dict(color=pos_color, width=0.5))
            else:
                timeout_marker = dict(symbol=8,
                                 line=dict(color=pos_color, width=0.5))

        else:
            timeout_marker = dict(symbol=0,
                                 line=dict(color=pos_color, width=0.5))

        if row['touchdown'] == 1:
            anno = 'TOUCHDOWN'
            if row['interception'] == 1:
                anno = 'PICK SIX'
                if row['posteam'] == row['away_team']:
                    yardage_change = (return_yards)
                else:
                    yardage_change = -(return_yards)
            elif row['fumble_lost'] == 1 or row['punt_blocked'] == 1:
                #anno = 'PICK SIX'
                if row['posteam'] == row['away_team']:
                    yardage_change = yard_line - yards_gained
                else:
                    yardage_change = -yard_line
            else:
                if row['posteam'] == row['away_team']:
                    yardage_change = -(yard_line)
                else:
                    yardage_change = yards_gained


        if row['punt_blocked'] == 1:
            pass
        elif row['play_type'] == 'kickoff' or row['play_type'] == 'punt':
            pos_color = 'white'
            yardage_marker = dict(line=dict(color='white'))
            no_play_flag = 1
            if row['touchdown'] == 1:
                #pos_color =
                yardage_marker = dict(line=dict(color=turnover_color))
                if row['posteam'] == row['away_team']:
                    yardage_change = yard_line - yards_gained
                else:
                    yardage_change = yard_line

        if 'PENALTY' in play_desc:
            no_play_flag = 1
            yardage_marker = dict(line=dict(
                                       color=pos_color,
                                       width=0.5),
                                  pattern=dict(
                                          shape='/',
                                          fgcolor='yellow',
                                          fgopacity=1)
                                  )



        if 'END QUARTER' in desc or 'GAME' in desc:
            fig.add_trace(go.Bar(x=[120],
                                 base=-10,
                                 y=[row['play_number']],
                                 hovertext=play_desc,
                                 orientation='h',
                                 marker_color='lightgray',
                                 width=1,
                                 marker=dict(
                                        line=dict(
                                             color='gray',
                                             width=0.5),
                                        #pattern=dict(shape='|', fgcolor='black', fgopacity=0.5))
                                        )
                                 )
                          )
            #if 'END QUARTER 1' in desc or 'END QUARTER 3' in desc:
            if desc == 'GAME':
                avg_play_number = -10
            elif desc == 'END QUARTER 1':
                last_play_number = 1
                avg_play_number = (play_number + last_play_number)/2
            else:
                #last_play_number = 20
                avg_play_number = (play_number + last_play_number)/2
                last_play_number = play_number

            if current_quarter == 5:
                quarter_anno = '<b>OT</b>'
            elif current_quarter == 4:
                quarter_anno = '<b>4th</b>'
            elif current_quarter == 3:
                quarter_anno = '<b>3rd</b>'
            elif current_quarter == 2:
                quarter_anno = '<b>2nd</b>'
            else:
                quarter_anno = '<b>1st</b>'

            fig.add_annotation(x=-5,
                               y=(avg_play_number),
                               text=quarter_anno,
                               showarrow=False,
                               font=dict(
                                    family="Courier New, monospace",
                                    size=18,
                                    color="lightgray"
                                    ),
                               ax=0,
                               ay=-10,
                               align="center",
                               opacity=1)
            current_quarter += 1
            last_play_number = play_number

            yard_numbers = [10,20,30,40,50,60,70,80,90]
            for i, number in enumerate(yard_numbers):
                if i < 5:
                    yard_number = number
                elif i == 5:
                    yard_number = 40
                elif i == 6:
                    yard_number = 30
                elif i == 7:
                    yard_number = 20
                else:
                    yard_number = 10
                fig.add_annotation(x=number,
                                   y=next_play_number,
                                   text=f'<b>{str(yard_number)}</b>',
                                   showarrow=True,
                                   font=dict(
                                        family="Courier New, monospace",
                                        size=18,
                                        color="gray"
                                        ),
                                   ax=0,
                                   ay=-10,
                                   align="center",
                                   opacity=1)
                fig.add_annotation(x=number,
                                   y=(next_play_number-3.1),
                                   text=f'<b>{str(yard_number)}</b>',
                                   showarrow=False,
                                   font=dict(
                                        family="Courier New, monospace",
                                        size=18,
                                        color="gray"
                                        ),
                                   ax=0,
                                   ay=0,
                                   align="center",
                                   opacity=1)


        elif no_play_flag != 0:
            if row['nextplay_actyrdln'] == 0 and row['touchdown'] == 0:
                if posteam == home_team:
                    yardage_change = (yards_gained)
                else:
                    yardage_change = -(yards_gained)
            fig.add_trace(go.Bar(x=[yardage_change],
                                 base=yard_line,
                                 y=[play_number],
                                 hovertext=play_desc,
                                 orientation='h',
                                 marker_color=pos_color,
                                 width=0.75,
                                 marker=yardage_marker,
                                 constraintext='outside',
                                 textfont=dict(
                                           family="Arial",
                                           #size=24,
                                           color='white'
                                           )
                                 )
                          )
        else:
            fig.add_trace(go.Scatter(x=[yard_line],
                                     y=[play_number],
                                     hovertext=play_desc,
                                     marker=timeout_marker,
                                     marker_color=pos_color
                                     )
                          )

        if anno != '':
            move_ax = 20
            move_ay = -20
            if row['quarter_seconds_remaining'] < 75:
                move_ax = -30
                move_ay = 30
            if row['touchdown'] == 1:
                if posteam == home_team:
                    yard_line = 100
                    move_ax = 40
                    move_ay = 0
                else:
                    yard_line = 0
                    move_ax = -40
                    move_ay = 0
            fig.add_annotation(x=yard_line,
                               y=play_number,
                               #xref="x",
                               #yref="y",
                               text=anno,
                               showarrow=True,
                               font=dict(
                                    family="Courier New, monospace",
                                    size=12,
                                    color="#ffffff"
                                    ),
                               align="center",
                               arrowhead=0,
                               arrowsize=0.5,
                               arrowwidth=1,
                               arrowcolor="gray",
                               ax=move_ax,
                               ay=move_ay,
                               bordercolor="lightgray",
                               borderwidth=1,
                               borderpad=2,
                               bgcolor=pos_color,
                               opacity=0.9
                               )



    fig.update_xaxes(gridwidth=0.25,
                     gridcolor='gray',
                     tickvals=[0,10,20,30,40,50,60,70,80,90,100],
                     showticklabels=False)
    fig.update_yaxes(visible=False)
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))


    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=wp_list, y=sorted(play_list),
                         line=dict(color='#222222', width=4)))

    if selected_game_df['away_score'].max() < selected_game_df['home_score'].max():

        fig2.add_trace(go.Bar(x=[.6], base=.5, y=[(selected_game_df['play_number'].max() + 0.25)],
                         orientation='h', marker_color=team_color_dict[row['home_team']], width=1,
                         marker=dict(line=dict(color='gray', width=0))
                         #pattern=dict(shape='|', fgcolor='black', fgopacity=0.5))
                         ))
    else:
        fig2.add_trace(go.Bar(x=[-.6], base=.5, y=[(selected_game_df['play_number'].max() + 0.25)],
                         orientation='h', marker_color=team_color_dict[row['away_team']], width=1,
                         marker=dict(line=dict(color='gray', width=0))
                         #pattern=dict(shape='|', fgcolor='black', fgopacity=0.5))
                         ))


    fig2.update_xaxes(gridwidth=0.25,
                      #linecolor='gray',
                      #spikecolor='gray',
                      #gridcolor='gray',
                      tickvals=[0,0.5,1],
                      showticklabels=False)

    fig2.add_annotation(x=0.5,
                       y=(next_play_number-5),
                       text='<b>Win<br>Probability</b>',
                       showarrow=False,
                       font=dict(
                            family="Courier New, monospace",
                            size=14,
                            color="gray"
                            ),
                       ax=0,
                       ay=0,
                       align="center",
                       opacity=1)

    fig2.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor='lightgray',
        xaxis=dict(range=[-0.05, 1.05], autorange=False, fixedrange=True),
        yaxis=dict(range=[0.5, (selected_game_df['next_play_number'].max() - 0.5)], autorange=False, fixedrange=True))


    fig2.update_yaxes(visible=False,
                      linecolor='gray',
                      spikecolor='gray')
    return fig, fig2

@app.callback(Output('game-info-text1', 'children'),
              Output('game-info-text2', 'children'),
              Output('game-info-text3', 'children'),
              Output('game-info-text4', 'children'),
              Output('game-info-text5', 'children'),
              Output('game-info-text6', 'children'),
              Output('game-info-text7', 'children'),
              Output('game-info-text8', 'children'),
              Output('game-info-text9', 'children'),
              Output('game-info-text10', 'children'),
              [Input('game-picker2', 'value')])
def update_text(selected_value):
    selected_game_df = df.loc[df['game_id'] == selected_value]
    away_team = selected_game_df['away_team'].max()
    away_score = selected_game_df['away_score'].max()
    home_team = selected_game_df['home_team'].max()
    home_score = selected_game_df['home_score'].max()
    total = away_score + home_score
    spread_result = home_score - away_score
    spread_line = selected_game_df['spread_line'].max()
    total_line = selected_game_df['total_line'].max()
    roof_type = selected_game_df['roof'].max()
    turf = selected_game_df['surface'].max()
    weather = selected_game_df['weather'].max()
    stadium = list(selected_game_df['game_stadium'])[0]

    weather = weather.replace('Temp:', '')
    weather = weather.replace('Humidity:', '')
    weather = weather.replace('Wind:', '')

    '''
    if len(weather) == 11:
        sky_cond = weather[0] + ' ' + weather[1]
        temp_cond = weather[3] + weather[4]
        wind_cond = weather[9] + ' ' + weather[10] + ' ' + weather[8]
        game_cond = f'{sky_cond}, {temp_cond} {wind_cond}, {turf.capitalize()}'
    #elif weather[0] == 'Controlled':
        #game_cond = f'Controlled, {turf.capitalize()}'
    else:
        sky_cond = weather[0]
        temp_cond = weather[2] + weather[3]
        wind_cond = weather[8] + ' ' + weather[9] + ' ' + weather[7]
        game_cond = f'{sky_cond}, {temp_cond} {wind_cond}, {turf.capitalize()}'

    #game_cond = f'{sky_cond}, {temp_cond} {wind_cond}, {turf.capitalize()}'
    #if roof_type == 'dome':
      #  game_cond = f'Dome {turf.capitalize()}'
    '''
    stats = selected_game_df.groupby(['posteam','play_type_nfl'])

    home_rush_yds = int(stats.get_group((home_team, 'RUSH'))['yards_gained'].sum())
    home_rush_atts = stats.get_group((home_team, 'RUSH'))['yards_gained'].count()
    home_rush_ypc = round(home_rush_yds/home_rush_atts, 1)
    home_rush_first = int(stats.get_group((home_team, 'RUSH'))['first_down'].sum())
    home_rush_tds = int(stats.get_group((home_team, 'RUSH'))['touchdown'].sum())
    away_rush_yds = int(stats.get_group((away_team, 'RUSH'))['yards_gained'].sum())
    away_rush_atts = stats.get_group((away_team, 'RUSH'))['yards_gained'].count()
    away_rush_ypc = round(away_rush_yds/away_rush_atts, 1)
    away_rush_first = int(stats.get_group((away_team, 'RUSH'))['first_down'].sum())
    away_rush_tds = int(stats.get_group((away_team, 'RUSH'))['touchdown'].sum())

    home_epa = round(selected_game_df.loc[selected_game_df['play_id'] == selected_game_df['play_id'].max()]['total_home_epa'].max(), 1)
    home_rush_epa = round(selected_game_df.loc[selected_game_df['play_id'] == selected_game_df['play_id'].max()]['total_home_rush_epa'].max(), 1)
    home_pass_epa = round(selected_game_df.loc[selected_game_df['play_id'] == selected_game_df['play_id'].max()]['total_home_pass_epa'].max(), 1)
    away_epa = round(selected_game_df.loc[selected_game_df['play_id'] == selected_game_df['play_id'].max()]['total_away_epa'].max(), 1)
    away_rush_epa = round(selected_game_df.loc[selected_game_df['play_id'] == selected_game_df['play_id'].max()]['total_away_rush_epa'].max(), 1)
    away_pass_epa = round(selected_game_df.loc[selected_game_df['play_id'] == selected_game_df['play_id'].max()]['total_away_pass_epa'].max(), 1)

    home_run_loc = stats.get_group((home_team, 'RUSH'))['run_location'].value_counts()
    away_run_loc = stats.get_group((away_team, 'RUSH'))['run_location'].value_counts()
    home_pass_loc = stats.get_group((home_team, 'PASS'))['pass_location'].value_counts()
    away_pass_loc = stats.get_group((away_team, 'PASS'))['pass_location'].value_counts()

    home_run_loc_dict = {}
    away_run_loc_dict = {}
    home_pass_loc_dict = {}
    away_pass_loc_dict = {}

    for loc in ['left', 'middle', 'right']:
        try:
            home_run_loc_dict.update({loc: home_run_loc[loc]})
            home_pass_loc_dict.update({loc: home_pass_loc[loc]})
        except:
            home_run_loc_dict.update({loc: 0})
            home_pass_loc_dict.update({loc: 0})
        try:
            away_run_loc_dict.update({loc: away_run_loc[loc]})
            away_pass_loc_dict.update({loc: away_pass_loc[loc]})
        except:
            away_run_loc_dict.update({loc: 0})
            away_pass_loc_dict.update({loc: 0})

    try:
        home_int = selected_game_df.loc[selected_game_df['interception'] == 1]['posteam'].value_counts()[away_team]
    except:
        home_int = 0

    try:
        away_int = selected_game_df.loc[selected_game_df['interception'] == 1]['posteam'].value_counts()[home_team]
    except:
        away_int = 0

    try:
        home_fumb = selected_game_df.loc[selected_game_df['fumble_lost'] == 1]['posteam'].value_counts()[away_team]
    except:
        home_fumb = 0

    try:
        away_fumb = selected_game_df.loc[selected_game_df['fumble_lost'] == 1]['posteam'].value_counts()[home_team]
    except:
        away_fumb = 0

    try:
        home_sacked_yds = abs(int(stats.get_group((away_team, 'SACK'))['yards_gained'].sum()))
        home_sacks = int(stats.get_group((away_team, 'SACK'))['yards_gained'].count())
    except:
        home_sacked_yds = 0

    try:
        away_sacked_yds = abs(int(stats.get_group((home_team, 'SACK'))['yards_gained'].sum()))
        away_sacks = int(stats.get_group((home_team, 'SACK'))['yards_gained'].count())
    except:
        away_sacked_yds = 0

    home_pass_yds = int(stats.get_group((home_team, 'PASS'))['yards_gained'].sum() + home_sacked_yds)
    home_pass_atts = int(stats.get_group((home_team, 'PASS'))['yards_gained'].count())
    home_pass_yac = int(stats.get_group((home_team, 'PASS'))['yards_after_catch'].sum())
    home_pass_airyds = int(stats.get_group((home_team, 'PASS'))['air_yards'].sum())
    home_pass_ypa = round(home_pass_yds/home_pass_atts, 1)
    home_pass_first = int(stats.get_group((home_team, 'PASS'))['first_down'].sum())
    home_pass_tds = int(stats.get_group((home_team, 'PASS'))['touchdown'].sum())
    away_pass_yds = int(stats.get_group((away_team, 'PASS'))['yards_gained'].sum() + away_sacked_yds)
    away_pass_atts = stats.get_group((away_team, 'PASS'))['yards_gained'].count()
    away_pass_yac = int(stats.get_group((away_team, 'PASS'))['yards_after_catch'].sum())
    away_pass_airyds = int(stats.get_group((away_team, 'PASS'))['air_yards'].sum())
    away_pass_ypa = round(away_pass_yds/away_pass_atts, 1)
    away_pass_first = int(stats.get_group((away_team, 'PASS'))['first_down'].sum())
    away_pass_tds = int(stats.get_group((away_team, 'PASS'))['touchdown'].sum())

    game_text1 = [
f'''*Away*: {away_team} {away_score}

''',
f'''*Home*: {home_team} {home_score}
''']
    game_text2 = [
f'''*Line*: {total_line}

*Total*: {total}
''']
    game_text3 = [
f'''*Spread*: {spread_line}

*Result*: {spread_result}''']
    game_text4 = [
f'''*Stadium*: {stadium}, {turf.capitalize()}

*Conditions*: {weather}''']
    game_text5 = [
f'''
![away logo](/assets/{away_team}_logo3.png)
''']
    game_text6 = [
f'''
![home logo](/assets/{home_team}_logo3.png)
''']

    game_text7 = [
f'''
![away logo](/assets/{away_team}_logo3.png)
''']
    game_text8 = [
f'''
![away logo](/assets/{home_team}_logo3.png)
''']
    game_text9 = [
f'''
**Game Stats**..

>EPA: {away_epa}

**Rushing**.....
>YDS: {away_rush_yds}

>ATT: {away_rush_atts}

>*Location*
> - &#x2190; {away_run_loc_dict["left"]}
> - &#x2191; {away_run_loc_dict["middle"]}
> - &#x2192; {away_run_loc_dict["right"]}

>YPC: {away_rush_ypc}

>EPA: {away_rush_epa}

>1ST: {away_rush_first}

>TD: {away_rush_tds}

**Passing**.....
>YDS: {away_pass_yds}

>ATT: {away_pass_atts}

>*Location*
> - &#x2190; {away_pass_loc_dict["left"]}
> - &#x2191; {away_pass_loc_dict["middle"]}
> - &#x2192; {away_pass_loc_dict["right"]}

>YAC: {away_pass_yac}

>AIR: {away_pass_airyds}

>YPA: {away_pass_ypa}

>EPA: {away_pass_epa}

>1ST: {away_pass_first}

>TD: {away_pass_tds}


**Defense**.....
>SACK: {away_sacks}

>SYDS: {away_sacked_yds}

>FUMB: {away_fumb}

>INT: {away_int}



''']
    game_text10 = [
f'''
............

>EPA: {home_epa}

............
>YDS: {home_rush_yds}

>ATT: {home_rush_atts}

>*Location*
> - &#x2190; {home_run_loc_dict["left"]}
> - &#x2191; {home_run_loc_dict["middle"]}
> - &#x2192; {home_run_loc_dict["right"]}

>YPC: {home_rush_ypc}

>EPA: {home_rush_epa}

>1ST: {home_rush_first}

>TD: {home_rush_tds}

............
>YDS: {home_pass_yds}

>ATT: {home_pass_atts}

>*Location*
> - &#x2190; {home_pass_loc_dict["left"]}
> - &#x2191; {home_pass_loc_dict["middle"]}
> - &#x2192; {home_pass_loc_dict["right"]}

>YAC: {home_pass_yac}

>AIR: {home_pass_airyds}

>YPA: {home_pass_ypa}

>EPA: {home_pass_epa}

>1ST: {home_pass_first}

>TD: {home_pass_tds}

............
>SACK: {home_sacks}

>SYDS: {home_sacked_yds}

>FUMB: {home_fumb}

>INT: {home_int}
''']


    return game_text1, game_text2, game_text3, game_text4, game_text5, game_text6, game_text7, game_text8, game_text9, game_text10

@app.callback(Output('playbyplay-graph', 'figure'),
              Output('wp-graph', 'figure'),
              [Input('game-picker2', 'value')])
def update_figure2(selected_value):
    fig, fig2 = create_playbyplay(selected_value)
    return fig, fig2

if __name__ == '__main__':
    app.run_server(debug=True)