{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Splitting data.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "3vIZzJbNQ7wq"
      },
      "source": [
        "#importing libraries\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UGJ8OELTSP1G"
      },
      "source": [
        "#Loading the data in python workspace using pandas\n",
        "dataset = pd.read_csv(\"Training_Data.csv\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jHAS86KsSj_M",
        "outputId": "92c62bff-7ded-4030-a4b6-df2b82e12d31"
      },
      "source": [
        "#Reading the dataset\n",
        "print(dataset)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "            Id   Income  Age  ...  CURRENT_JOB_YRS CURRENT_HOUSE_YRS Risk_Flag\n",
            "0            1  1303834   23  ...                3                13         0\n",
            "1            2  7574516   40  ...                9                13         0\n",
            "2            3  3991815   66  ...                4                10         0\n",
            "3            4  6256451   41  ...                2                12         1\n",
            "4            5  5768871   47  ...                3                14         1\n",
            "...        ...      ...  ...  ...              ...               ...       ...\n",
            "251995  251996  8154883   43  ...                6                11         0\n",
            "251996  251997  2843572   26  ...                6                11         0\n",
            "251997  251998  4522448   46  ...                7                12         0\n",
            "251998  251999  6507128   45  ...                0                10         0\n",
            "251999  252000  9070230   70  ...                7                11         0\n",
            "\n",
            "[252000 rows x 13 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 224
        },
        "id": "L6zQePhvSkJ7",
        "outputId": "2c563e0d-7c23-49e5-8736-e7d2ea1affa0"
      },
      "source": [
        "#To see the first five rows \n",
        "dataset.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Id</th>\n",
              "      <th>Income</th>\n",
              "      <th>Age</th>\n",
              "      <th>Experience</th>\n",
              "      <th>Married/Single</th>\n",
              "      <th>House_Ownership</th>\n",
              "      <th>Car_Ownership</th>\n",
              "      <th>Profession</th>\n",
              "      <th>CITY</th>\n",
              "      <th>STATE</th>\n",
              "      <th>CURRENT_JOB_YRS</th>\n",
              "      <th>CURRENT_HOUSE_YRS</th>\n",
              "      <th>Risk_Flag</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1303834</td>\n",
              "      <td>23</td>\n",
              "      <td>3</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Mechanical_engineer</td>\n",
              "      <td>Rewa</td>\n",
              "      <td>Madhya_Pradesh</td>\n",
              "      <td>3</td>\n",
              "      <td>13</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>7574516</td>\n",
              "      <td>40</td>\n",
              "      <td>10</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Software_Developer</td>\n",
              "      <td>Parbhani</td>\n",
              "      <td>Maharashtra</td>\n",
              "      <td>9</td>\n",
              "      <td>13</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>3991815</td>\n",
              "      <td>66</td>\n",
              "      <td>4</td>\n",
              "      <td>married</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Technical_writer</td>\n",
              "      <td>Alappuzha</td>\n",
              "      <td>Kerala</td>\n",
              "      <td>4</td>\n",
              "      <td>10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>6256451</td>\n",
              "      <td>41</td>\n",
              "      <td>2</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>yes</td>\n",
              "      <td>Software_Developer</td>\n",
              "      <td>Bhubaneswar</td>\n",
              "      <td>Odisha</td>\n",
              "      <td>2</td>\n",
              "      <td>12</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>5768871</td>\n",
              "      <td>47</td>\n",
              "      <td>11</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Civil_servant</td>\n",
              "      <td>Tiruchirappalli[10]</td>\n",
              "      <td>Tamil_Nadu</td>\n",
              "      <td>3</td>\n",
              "      <td>14</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Id   Income  Age  ...  CURRENT_JOB_YRS CURRENT_HOUSE_YRS Risk_Flag\n",
              "0   1  1303834   23  ...                3                13         0\n",
              "1   2  7574516   40  ...                9                13         0\n",
              "2   3  3991815   66  ...                4                10         0\n",
              "3   4  6256451   41  ...                2                12         1\n",
              "4   5  5768871   47  ...                3                14         1\n",
              "\n",
              "[5 rows x 13 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 317
        },
        "id": "rQBaInbnSkNJ",
        "outputId": "852e2937-fca9-4f2d-d204-f961923dbb41"
      },
      "source": [
        "#To get the summary of the dataset (numarical values)\n",
        "dataset.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Id</th>\n",
              "      <th>Income</th>\n",
              "      <th>Age</th>\n",
              "      <th>Experience</th>\n",
              "      <th>CURRENT_JOB_YRS</th>\n",
              "      <th>CURRENT_HOUSE_YRS</th>\n",
              "      <th>Risk_Flag</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>252000.000000</td>\n",
              "      <td>2.520000e+05</td>\n",
              "      <td>252000.000000</td>\n",
              "      <td>252000.000000</td>\n",
              "      <td>252000.000000</td>\n",
              "      <td>252000.000000</td>\n",
              "      <td>252000.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>126000.500000</td>\n",
              "      <td>4.997117e+06</td>\n",
              "      <td>49.954071</td>\n",
              "      <td>10.084437</td>\n",
              "      <td>6.333877</td>\n",
              "      <td>11.997794</td>\n",
              "      <td>0.123000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>72746.278255</td>\n",
              "      <td>2.878311e+06</td>\n",
              "      <td>17.063855</td>\n",
              "      <td>6.002590</td>\n",
              "      <td>3.647053</td>\n",
              "      <td>1.399037</td>\n",
              "      <td>0.328438</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.031000e+04</td>\n",
              "      <td>21.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>63000.750000</td>\n",
              "      <td>2.503015e+06</td>\n",
              "      <td>35.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>11.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>126000.500000</td>\n",
              "      <td>5.000694e+06</td>\n",
              "      <td>50.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>189000.250000</td>\n",
              "      <td>7.477502e+06</td>\n",
              "      <td>65.000000</td>\n",
              "      <td>15.000000</td>\n",
              "      <td>9.000000</td>\n",
              "      <td>13.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>252000.000000</td>\n",
              "      <td>9.999938e+06</td>\n",
              "      <td>79.000000</td>\n",
              "      <td>20.000000</td>\n",
              "      <td>14.000000</td>\n",
              "      <td>14.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                  Id        Income  ...  CURRENT_HOUSE_YRS      Risk_Flag\n",
              "count  252000.000000  2.520000e+05  ...      252000.000000  252000.000000\n",
              "mean   126000.500000  4.997117e+06  ...          11.997794       0.123000\n",
              "std     72746.278255  2.878311e+06  ...           1.399037       0.328438\n",
              "min         1.000000  1.031000e+04  ...          10.000000       0.000000\n",
              "25%     63000.750000  2.503015e+06  ...          11.000000       0.000000\n",
              "50%    126000.500000  5.000694e+06  ...          12.000000       0.000000\n",
              "75%    189000.250000  7.477502e+06  ...          13.000000       0.000000\n",
              "max    252000.000000  9.999938e+06  ...          14.000000       1.000000\n",
              "\n",
              "[8 rows x 7 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8MdxA9k3SkQw",
        "outputId": "ea6af885-d85c-4a6d-fb30-c329c3f4736a"
      },
      "source": [
        "#Checking for the duplicate values \n",
        "dataset.duplicated()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0         False\n",
              "1         False\n",
              "2         False\n",
              "3         False\n",
              "4         False\n",
              "          ...  \n",
              "251995    False\n",
              "251996    False\n",
              "251997    False\n",
              "251998    False\n",
              "251999    False\n",
              "Length: 252000, dtype: bool"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 439
        },
        "id": "zcdT0GD6Wmo3",
        "outputId": "aff44936-a9de-497f-dd14-d8772cf2fbba"
      },
      "source": [
        "dataset.drop_duplicates()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Id</th>\n",
              "      <th>Income</th>\n",
              "      <th>Age</th>\n",
              "      <th>Experience</th>\n",
              "      <th>Married/Single</th>\n",
              "      <th>House_Ownership</th>\n",
              "      <th>Car_Ownership</th>\n",
              "      <th>Profession</th>\n",
              "      <th>CITY</th>\n",
              "      <th>STATE</th>\n",
              "      <th>CURRENT_JOB_YRS</th>\n",
              "      <th>CURRENT_HOUSE_YRS</th>\n",
              "      <th>Risk_Flag</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1303834</td>\n",
              "      <td>23</td>\n",
              "      <td>3</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Mechanical_engineer</td>\n",
              "      <td>Rewa</td>\n",
              "      <td>Madhya_Pradesh</td>\n",
              "      <td>3</td>\n",
              "      <td>13</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>7574516</td>\n",
              "      <td>40</td>\n",
              "      <td>10</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Software_Developer</td>\n",
              "      <td>Parbhani</td>\n",
              "      <td>Maharashtra</td>\n",
              "      <td>9</td>\n",
              "      <td>13</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>3991815</td>\n",
              "      <td>66</td>\n",
              "      <td>4</td>\n",
              "      <td>married</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Technical_writer</td>\n",
              "      <td>Alappuzha</td>\n",
              "      <td>Kerala</td>\n",
              "      <td>4</td>\n",
              "      <td>10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>6256451</td>\n",
              "      <td>41</td>\n",
              "      <td>2</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>yes</td>\n",
              "      <td>Software_Developer</td>\n",
              "      <td>Bhubaneswar</td>\n",
              "      <td>Odisha</td>\n",
              "      <td>2</td>\n",
              "      <td>12</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>5768871</td>\n",
              "      <td>47</td>\n",
              "      <td>11</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Civil_servant</td>\n",
              "      <td>Tiruchirappalli[10]</td>\n",
              "      <td>Tamil_Nadu</td>\n",
              "      <td>3</td>\n",
              "      <td>14</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251995</th>\n",
              "      <td>251996</td>\n",
              "      <td>8154883</td>\n",
              "      <td>43</td>\n",
              "      <td>13</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Surgeon</td>\n",
              "      <td>Kolkata</td>\n",
              "      <td>West_Bengal</td>\n",
              "      <td>6</td>\n",
              "      <td>11</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251996</th>\n",
              "      <td>251997</td>\n",
              "      <td>2843572</td>\n",
              "      <td>26</td>\n",
              "      <td>10</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Army_officer</td>\n",
              "      <td>Rewa</td>\n",
              "      <td>Madhya_Pradesh</td>\n",
              "      <td>6</td>\n",
              "      <td>11</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251997</th>\n",
              "      <td>251998</td>\n",
              "      <td>4522448</td>\n",
              "      <td>46</td>\n",
              "      <td>7</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Design_Engineer</td>\n",
              "      <td>Kalyan-Dombivli</td>\n",
              "      <td>Maharashtra</td>\n",
              "      <td>7</td>\n",
              "      <td>12</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251998</th>\n",
              "      <td>251999</td>\n",
              "      <td>6507128</td>\n",
              "      <td>45</td>\n",
              "      <td>0</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Graphic_Designer</td>\n",
              "      <td>Pondicherry</td>\n",
              "      <td>Puducherry</td>\n",
              "      <td>0</td>\n",
              "      <td>10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251999</th>\n",
              "      <td>252000</td>\n",
              "      <td>9070230</td>\n",
              "      <td>70</td>\n",
              "      <td>17</td>\n",
              "      <td>single</td>\n",
              "      <td>rented</td>\n",
              "      <td>no</td>\n",
              "      <td>Statistician</td>\n",
              "      <td>Avadi</td>\n",
              "      <td>Tamil_Nadu</td>\n",
              "      <td>7</td>\n",
              "      <td>11</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>252000 rows × 13 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "            Id   Income  Age  ...  CURRENT_JOB_YRS CURRENT_HOUSE_YRS Risk_Flag\n",
              "0            1  1303834   23  ...                3                13         0\n",
              "1            2  7574516   40  ...                9                13         0\n",
              "2            3  3991815   66  ...                4                10         0\n",
              "3            4  6256451   41  ...                2                12         1\n",
              "4            5  5768871   47  ...                3                14         1\n",
              "...        ...      ...  ...  ...              ...               ...       ...\n",
              "251995  251996  8154883   43  ...                6                11         0\n",
              "251996  251997  2843572   26  ...                6                11         0\n",
              "251997  251998  4522448   46  ...                7                12         0\n",
              "251998  251999  6507128   45  ...                0                10         0\n",
              "251999  252000  9070230   70  ...                7                11         0\n",
              "\n",
              "[252000 rows x 13 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eu9GMB7yVNFg",
        "outputId": "fd77e25f-767b-47be-d211-1533e8d7a054"
      },
      "source": [
        "print(\"No duplicate Values\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "No duplicate Values\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 439
        },
        "id": "LYMus56PVzxQ",
        "outputId": "f50ea8b9-b41a-4849-fda4-a94a53da7bac"
      },
      "source": [
        "#checking for the missing values\n",
        "dataset.isnull()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Id</th>\n",
              "      <th>Income</th>\n",
              "      <th>Age</th>\n",
              "      <th>Experience</th>\n",
              "      <th>Married/Single</th>\n",
              "      <th>House_Ownership</th>\n",
              "      <th>Car_Ownership</th>\n",
              "      <th>Profession</th>\n",
              "      <th>CITY</th>\n",
              "      <th>STATE</th>\n",
              "      <th>CURRENT_JOB_YRS</th>\n",
              "      <th>CURRENT_HOUSE_YRS</th>\n",
              "      <th>Risk_Flag</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251995</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251996</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251997</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251998</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>251999</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>252000 rows × 13 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "           Id  Income    Age  ...  CURRENT_JOB_YRS  CURRENT_HOUSE_YRS  Risk_Flag\n",
              "0       False   False  False  ...            False              False      False\n",
              "1       False   False  False  ...            False              False      False\n",
              "2       False   False  False  ...            False              False      False\n",
              "3       False   False  False  ...            False              False      False\n",
              "4       False   False  False  ...            False              False      False\n",
              "...       ...     ...    ...  ...              ...                ...        ...\n",
              "251995  False   False  False  ...            False              False      False\n",
              "251996  False   False  False  ...            False              False      False\n",
              "251997  False   False  False  ...            False              False      False\n",
              "251998  False   False  False  ...            False              False      False\n",
              "251999  False   False  False  ...            False              False      False\n",
              "\n",
              "[252000 rows x 13 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D-zpak-BWdkr",
        "outputId": "31186bbb-ad71-492b-a354-fabf242f2e10"
      },
      "source": [
        "#Counting the number of null values in each columns\n",
        "dataset.isnull().sum()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Id                   0\n",
              "Income               0\n",
              "Age                  0\n",
              "Experience           0\n",
              "Married/Single       0\n",
              "House_Ownership      0\n",
              "Car_Ownership        0\n",
              "Profession           0\n",
              "CITY                 0\n",
              "STATE                0\n",
              "CURRENT_JOB_YRS      0\n",
              "CURRENT_HOUSE_YRS    0\n",
              "Risk_Flag            0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N_wASOwqWuYX",
        "outputId": "aba9c4ea-0e53-47f3-d5a0-c3c0d199a966"
      },
      "source": [
        "#As there is no missing vales no need for mode imputation\n",
        "if(sum(dataset.isnull().sum()) == 0):\n",
        "  print(\"No missing values\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "No missing values\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uby5yoaoW37a",
        "outputId": "04e0033f-d528-486b-9cf8-c5c43d392a7a"
      },
      "source": [
        "#Reading the columns\n",
        "dataset.columns"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Id', 'Income', 'Age', 'Experience', 'Married/Single',\n",
              "       'House_Ownership', 'Car_Ownership', 'Profession', 'CITY', 'STATE',\n",
              "       'CURRENT_JOB_YRS', 'CURRENT_HOUSE_YRS', 'Risk_Flag'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "c1avrIeWXb6O"
      },
      "source": [
        "#Splitting the data into independent and dependent \n",
        "X = dataset[['Id','Income', 'Age', 'Experience','Married/Single',\n",
        "       'House_Ownership', 'Car_Ownership', 'Profession', 'CITY', 'STATE',\n",
        "       'CURRENT_JOB_YRS', 'CURRENT_HOUSE_YRS']].values\n",
        "\n",
        "Y = dataset['Risk_Flag'].values"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "puqKicLLX0Cg",
        "outputId": "4c4b3f38-b179-4288-a468-5adf4e6fe14f"
      },
      "source": [
        "print(X)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[1 1303834 23 ... 'Madhya_Pradesh' 3 13]\n",
            " [2 7574516 40 ... 'Maharashtra' 9 13]\n",
            " [3 3991815 66 ... 'Kerala' 4 10]\n",
            " ...\n",
            " [251998 4522448 46 ... 'Maharashtra' 7 12]\n",
            " [251999 6507128 45 ... 'Puducherry' 0 10]\n",
            " [252000 9070230 70 ... 'Tamil_Nadu' 7 11]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RWr6FYoTX1xc",
        "outputId": "ac8692f2-36ba-4679-ae23-4c3d85496faf"
      },
      "source": [
        "print(Y)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0 0 0 ... 0 0 0]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BoZeHt_yYmNq",
        "outputId": "572149df-dec0-4420-c02a-edccadaa9e42"
      },
      "source": [
        "print(X[0])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1 1303834 23 3 'single' 'rented' 'no' 'Mechanical_engineer' 'Rewa'\n",
            " 'Madhya_Pradesh' 3 13]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XGoOpZ9zX3Cd"
      },
      "source": [
        "#using label encoder to convert the categorical values which have two values\n",
        "from sklearn.preprocessing import LabelEncoder\n",
        "le = LabelEncoder()\n",
        "X[:,4] = le.fit_transform(X[:,4])\n",
        "X[:,5] = le.fit_transform(X[:,5])\n",
        "X[:,6] = le.fit_transform(X[:,6])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lL07PMMAO0qW",
        "outputId": "9658a8d7-3c6c-417c-bd72-7638a76e9bec"
      },
      "source": [
        "#As the data is converting into tuple we consider the first 10 rows\n",
        "print(X[0])\n",
        "X=X[:10]\n",
        "Y=Y[:10]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1 1303834 23 3 1 2 0 'Mechanical_engineer' 'Rewa' 'Madhya_Pradesh' 3 13]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2TDqj8Q_Y9pZ",
        "outputId": "5614366b-d4ad-4912-c980-62d1fa46ff14"
      },
      "source": [
        "# Handling Categorical Data\n",
        "from sklearn.compose import ColumnTransformer\n",
        "from sklearn.preprocessing import OneHotEncoder\n",
        "\n",
        "ct = ColumnTransformer(transformers=[('enconder', OneHotEncoder(), [7,8,9])], remainder='passthrough')\n",
        "\n",
        "X = np.array(ct.fit_transform(X))\n",
        "print(X)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0\n",
            "  0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 1 1303834 23 3 1 2 0 3 13]\n",
            " [0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 2 7574516 40 10 1 2 0 9 13]\n",
            " [0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 3 3991815 66 4 0 2 0 4 10]\n",
            " [0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 4 6256451 41 2 1 2 1 2 12]\n",
            " [0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0\n",
            "  0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 5 5768871 47 11 1 2 0 3 14]\n",
            " [0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 6 6915937 64 0 1 2 0 0 12]\n",
            " [0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0\n",
            "  0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 7 3954973 58 14 0 2 0 8 12]\n",
            " [0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 8 1706172 33 2 1 2 0 2 14]\n",
            " [0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 9 7566849 24 17 1 2 1 11 11]\n",
            " [1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 10 8964846 23 12 1 2 0 5 13]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BdpjTWPdZXtS"
      },
      "source": [
        "# Splitting Dataset into Training and Test Set\n",
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f6VDq-y-Z-55",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "60e5518b-1f24-4912-9d17-28e70fb7aa58"
      },
      "source": [
        "print(X_train)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 8 1706172 33 2 1 2 0 2 14]\n",
            " [0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 3 3991815 66 4 0 2 0 4 10]\n",
            " [0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 4 6256451 41 2 1 2 1 2 12]\n",
            " [0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0\n",
            "  0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 7 3954973 58 14 0 2 0 8 12]\n",
            " [1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 10 8964846 23 12 1 2 0 5 13]\n",
            " [0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 9 7566849 24 17 1 2 1 11 11]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "19O1ojFlPS0n",
        "outputId": "4756579a-819d-45ec-bcb1-8da2755c663a"
      },
      "source": [
        "print(X_test)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0\n",
            "  0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 5 5768871 47 11 1 2 0 3 14]\n",
            " [0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 2 7574516 40 10 1 2 0 9 13]\n",
            " [0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 6 6915937 64 0 1 2 0 0 12]\n",
            " [0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0\n",
            "  0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 1 1303834 23 3 1 2 0 3 13]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2JKfdRyGPVXI",
        "outputId": "90206504-1c42-4993-f87d-ab6cd28aff1b"
      },
      "source": [
        "print(y_train)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0 0 1 0 0 0]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pIvCmHSvPjmu",
        "outputId": "6846ed0f-fa97-4bb1-8031-34489e42cb35"
      },
      "source": [
        "print(y_test)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1 0 0 0]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xuEFPwzMPlMF"
      },
      "source": [
        "# Feature Scaling\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "sc = StandardScaler()\n",
        "X_train[:, 4:] = sc.fit_transform(X_train[:, 4:])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eP5VlCNkPu1q",
        "outputId": "7af96e4f-c17e-4882-f2b9-7b681c014277"
      },
      "source": [
        "print(X_train)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[0.0 0.0 1.0 0.0 -0.44721359549995787 0.0 -0.44721359549995787\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  2.2360679774997894 -0.4472135954999579 -0.44721359549995787 0.0 0.0 0.0\n",
            "  -0.44721359549995787 2.2360679774997894 -0.44721359549995787 0.0 0.0\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787\n",
            "  -0.4472135954999579 0.45858524745629303 -1.5139101299420386\n",
            "  -0.4810717910026329 -1.074661571986846 0.7071067811865476 0.0\n",
            "  -0.7071067811865475 -1.025978352085154 1.5491933384829668]\n",
            " [0.0 0.0 0.0 0.0 -0.44721359549995787 0.0 -0.44721359549995787\n",
            "  2.2360679774997894 2.2360679774997894 -0.44721359549995787 0.0\n",
            "  -0.44721359549995787 -0.4472135954999579 -0.44721359549995787 0.0 0.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 2.2360679774997894 0.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787\n",
            "  -0.4472135954999579 -1.5067800987849622 -0.5788768316929576\n",
            "  1.5455710732212244 -0.7439964729139703 -1.414213562373095 0.0\n",
            "  -0.7071067811865475 -0.41039134083406154 -1.5491933384829668]\n",
            " [0.0 0.0 0.0 0.0 -0.44721359549995787 0.0 2.2360679774997894\n",
            "  -0.44721359549995787 -0.44721359549995787 2.2360679774997894 0.0\n",
            "  -0.44721359549995787 -0.4472135954999579 -0.44721359549995787 0.0 0.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  0.0 2.2360679774997894 -0.44721359549995787 -0.44721359549995787\n",
            "  -0.4472135954999579 -1.1137070295367113 0.34756271657140647\n",
            "  0.010235570021332468 -1.074661571986846 0.7071067811865476 0.0\n",
            "  1.4142135623730951 -1.025978352085154 0.0]\n",
            " [0.0 0.0 0.0 0.0 2.2360679774997894 0.0 -0.44721359549995787\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  -0.44721359549995787 -0.4472135954999579 -0.44721359549995787 0.0 0.0\n",
            "  0.0 2.2360679774997894 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 2.2360679774997894\n",
            "  -0.4472135954999579 0.06551217820804196 -0.5939485190798734\n",
            "  1.054263712197259 0.9093290224504081 -1.414213562373095 0.0\n",
            "  -0.7071067811865475 0.8207826816681234 0.0]\n",
            " [1.0 0.0 0.0 0.0 -0.44721359549995787 0.0 -0.44721359549995787\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  -0.44721359549995787 2.23606797749979 -0.44721359549995787 0.0 0.0 0.0\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0 0.0\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787\n",
            "  2.23606797749979 1.244731385952795 1.4555395571415741\n",
            "  -1.0952059922825896 0.5786639233775325 0.7071067811865476 0.0\n",
            "  -0.7071067811865475 -0.10259783520851533 0.7745966692414834]\n",
            " [0.0 0.0 0.0 1.0 -0.44721359549995787 0.0 -0.44721359549995787\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  -0.44721359549995787 -0.4472135954999579 2.2360679774997894 0.0 0.0 0.0\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0 0.0\n",
            "  -0.44721359549995787 2.2360679774997894 -0.44721359549995787\n",
            "  -0.4472135954999579 0.8516583167045441 0.8836332070018889\n",
            "  -1.033792572154594 1.4053266710597219 0.7071067811865476 0.0\n",
            "  1.4142135623730951 1.744163198544762 -0.7745966692414834]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZoMlqiZ_Pxbi",
        "outputId": "baa7ba18-1cde-4828-f85a-bbb683622427"
      },
      "source": [
        "print(X_test)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0\n",
            "  0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 5 5768871 47 11 1 2 0 3 14]\n",
            " [0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 2 7574516 40 10 1 2 0 9 13]\n",
            " [0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n",
            "  0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 6 6915937 64 0 1 2 0 0 12]\n",
            " [0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0\n",
            "  0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 1 1303834 23 3 1 2 0 3 13]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LA25iz1XP0zg",
        "outputId": "65ddfd85-46ef-452a-d410-e87e89b95b57"
      },
      "source": [
        "X_test[:, 4:] = sc.transform(X_test[:, 4:])\n",
        "print(X_test)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[0.0 1.0 0.0 0.0 -0.44721359549995787 0.0 -0.44721359549995787\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  -0.44721359549995787 -0.4472135954999579 -0.44721359549995787 0.0 0.0\n",
            "  1.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 2.2360679774997894\n",
            "  -0.4472135954999579 -0.7206339602884602 0.1480986989797323\n",
            "  0.3787160907893065 0.41333137384109464 0.7071067811865476 0.0\n",
            "  -0.7071067811865475 -0.7181848464596078 1.5491933384829668]\n",
            " [0.0 0.0 0.0 0.0 -0.44721359549995787 0.0 2.2360679774997894\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  -0.44721359549995787 -0.4472135954999579 -0.44721359549995787 1.0 0.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  1.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787\n",
            "  -0.4472135954999579 -1.8998531680332134 0.8867696987014569\n",
            "  -0.05117785010666321 0.24799882430465678 0.7071067811865476 0.0\n",
            "  -0.7071067811865475 1.1285761872936697 0.7745966692414834]\n",
            " [0.0 1.0 0.0 0.0 -0.44721359549995787 0.0 -0.44721359549995787\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 1.0\n",
            "  -0.44721359549995787 -0.4472135954999579 -0.44721359549995787 0.0 0.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  1.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787\n",
            "  -0.4472135954999579 -0.3275608910402091 0.6173517298727371\n",
            "  1.4227442329652331 -1.4053266710597219 0.7071067811865476 0.0\n",
            "  -0.7071067811865475 -1.6415653633362466 0.0]\n",
            " [0.0 0.0 0.0 0.0 -0.44721359549995787 1.0 -0.44721359549995787\n",
            "  -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 0.0\n",
            "  -0.44721359549995787 -0.4472135954999579 -0.44721359549995787 0.0 1.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787 1.0\n",
            "  0.0 -0.44721359549995787 -0.44721359549995787 -0.44721359549995787\n",
            "  -0.4472135954999579 -2.2929262372814643 -1.6785025125455066\n",
            "  -1.0952059922825896 -0.9093290224504081 0.7071067811865476 0.0\n",
            "  -0.7071067811865475 -0.7181848464596078 0.7745966692414834]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1XAMq5a0P2-O"
      },
      "source": [
        "#writing the split data as test and train data\n",
        "DF = pd.DataFrame(X_train)\n",
        "DF.to_csv(\"train.csv\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qnDc_tliQJB3"
      },
      "source": [
        "df = pd.DataFrame(X_test)\n",
        "df.to_csv(\"test.csv\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-5pDfSOGQK7T"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}