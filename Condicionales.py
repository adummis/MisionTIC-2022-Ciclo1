{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Condicionales.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNwPyP0/c55cmHwKiCjFh7N",
      "include_colab_link": True,
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/NestorRodriguez/MisionTIC-2022-Ciclo1/blob/main/Condicionales.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Condicional con tipo de dato Boolean"
      ],
      "metadata": {
        "id": "L9eE9So9w0tf"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HACnuTlzwJh2",
        "outputId": "38473d75-ec75-446e-ef76-31dff1c82c5a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Valor falso\n"
          ]
        }
      ],
      "source": [
        "valor = False\n",
        "if valor:\n",
        "  print('valor verdadero')\n",
        "else:\n",
        "  print('Valor falso')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Condicional con valor int, float"
      ],
      "metadata": {
        "id": "By8A3Mv6wzTs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "valor = 3\n",
        "# Formato de una condición\n",
        "# 1. variable\n",
        "# 2. Operador lógico\n",
        "# 3. Valor a comparar\n",
        "if valor > 5:\n",
        "  print('La variable es mayor a 5')\n",
        "  print('Si es mayor')\n",
        "else:\n",
        "  print('La variable es menor a 5')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pJHH93iHwy0_",
        "outputId": "033142ca-0d81-48dc-8cc2-f4c7bcc3424d"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "La variable es menor a 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Condicional con string"
      ],
      "metadata": {
        "id": "rRzQ_9Bbwxfr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "palabra = 'Mamá'\n",
        "# Formato de una condición\n",
        "# 1. variable\n",
        "# 2. Operador lógico\n",
        "# 3. Valor a comparar\n",
        "if palabra == 'mamá':\n",
        "  print('Si es sigual')\n",
        "else:\n",
        "  print('No es mamá')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NVGN_yA8-cg4",
        "outputId": "8c913c6e-f3d5-4187-e9db-f154f5e22367"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "No es mamá\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Condicionales aninadas"
      ],
      "metadata": {
        "id": "dQ1HDK68HlrB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "color = 'turquesa'\n",
        "if color == 'verde':\n",
        "  print('Si es verde')\n",
        "#else if\n",
        "elif color == 'azul':\n",
        "  print('Si es azul')\n",
        "elif color == 'rojo':\n",
        "  print('Si es rojo')\n",
        "elif color == 'amarillo':\n",
        "  print('Si es amarillo')\n",
        "else:\n",
        "  print('Es otro color diferente')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XQAqgeCyHtpk",
        "outputId": "23322a1a-8dca-46e9-ed7c-6c90a28ba425"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Es otro color diferente\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ejercicio: Se desea crear un algoritmo que permita si un estudiante aprobo o no aprobo la materia. La nota de aprobación es 3.0"
      ],
      "metadata": {
        "id": "X8tOM3tPJ2aB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nota = 4.0\n",
        "if nota < 3.0:\n",
        "  print('No aprobo')\n",
        "else:\n",
        "  print('Aprobo')\n",
        "\n",
        "if nota >= 3.0:\n",
        "  print('Aprobo')\n",
        "else:\n",
        "  print('No aprobo')\n",
        "\n",
        "if nota > 2.9:\n",
        "  print('Aprobo')\n",
        "else:\n",
        "  print('No aprobo')\n",
        "\n",
        "if nota < 0:\n",
        "  print('Error en la nota')\n",
        "elif nota > 5:\n",
        "  print('Error en la nota')\n",
        "elif nota < 3.0:\n",
        "  print('No aprobo')\n",
        "elif nota >= 3.0:\n",
        "  print('Aprobo')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u44-873NKD7o",
        "outputId": "7ddca803-f6d4-484e-e10c-a3bd4fa9aa7c"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Aprobo\n",
            "Aprobo\n",
            "Aprobo\n",
            "Aprobo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Input"
      ],
      "metadata": {
        "id": "JEEe8Z9aNVCz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('Digite la nota')\n",
        "nota = float(input())\n",
        "if nota > 2.9:\n",
        "  print('Aprobo')\n",
        "else:\n",
        "  print('No aprobo')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nS55iEToNXR4",
        "outputId": "d0c760fe-6279-4937-cfa1-41b25494bc7a"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite la nota\n",
            "3.0\n",
            "Aprobo\n"
          ]
        }
      ]
    }
  ]
}